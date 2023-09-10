import pygame
from sys import exit
from random import randint
from game import Game
from player import Player
from projectile import Projectile
from enemy import Enemy

# Initialize pygame subsystems
pygame.init()

version = " v0.0.6"

# Set up window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
caption = f"Sacred Flame {version}"
pygame.display.set_caption(caption)

# Game state object
game = Game()

# Surfaces
backgroundSurface = pygame.image.load('graphics/bg-blue.png').convert_alpha()

# Player variables

# Groups
# Player group
player = pygame.sprite.GroupSingle()
player.add(Player(SCREEN_WIDTH, SCREEN_HEIGHT))

# Projectile group
projectileGroup = pygame.sprite.Group()

# Enemy group
enemyGroup = pygame.sprite.Group()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Fonts

# TODO: determine final font style

# Start of game font
startFont = pygame.font.SysFont('freesansbold', 32)
startText = startFont.render("Press SPACE to begin", True, white, black) 
startTextRect = startText.get_rect()
startTextRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Pause screen font
pauseFont = pygame.font.SysFont('freesansbold', 32)
pauseText = pauseFont.render("Game paused", True, white, black) 
pauseTextRect = pauseText.get_rect()
pauseTextRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Game over screen font
deathFont = pygame.font.SysFont('freesansbold', 32)
deathText = deathFont.render("You Died", True, white, black) 
deathTextRect = deathText.get_rect()
deathTextRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Music

# Clock and timers
clock = pygame.time.Clock()

enemyTimer = pygame.USEREVENT + 1
eventRate = 1500
pygame.time.set_timer(enemyTimer, eventRate)

# Functions
def SpawnEnemy(SCREEN_WIDTH, SCREEN_HEIGHT):
    
    spawnX = randint(0, SCREEN_WIDTH)
    spawnY = randint(0, SCREEN_HEIGHT)
    spawn = (spawnX, spawnY)

    e = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT, spawn, "basic")
    return e

def GameRestart():
    enemyGroup.empty()
    player.sprite.Restart()
    game.Update('rInput')
    print(" restart")

def GameStart():
    game.Update('spaceInput')
    print(" start")


# Create projectile at position of player and give direction
def FireProjectile(posX, posY, direction):
    p = Projectile(SCREEN_WIDTH, SCREEN_HEIGHT, posX, posY)
    if direction == "up":
        p.vy = -1
    if direction == "down":
        p.vy = 1
    if direction == "left":
        p.vx = -1
    if direction == "right":
        p.vx = 1
    projectileGroup.add(p)

# Shutdown pygame and exit program.
def QuitGame():
    pygame.quit()
    exit()

def main():

    # Begin main game loop
    while True:
        
        # Begin event loop
        # Get event from queue
        for event in pygame.event.get():
            # on window close
            if event.type == pygame.QUIT:
                QuitGame()

            # On keypress
            if event.type == pygame.KEYDOWN:

                # Close window on escape press
                if event.key == pygame.K_ESCAPE:
                    QuitGame()
                if event.key == pygame.K_SPACE:
                    if game.currentState == 'title':
                        GameStart()
                if event.key == pygame.K_p:
                    # pause game
                    game.Update('pInput')
                if event.key == pygame.K_r:
                    if game.currentState == 'gameLose':
                        GameRestart()
                # get player input
                if game.IsRunning():
                    if event.key == pygame.K_UP:
                        FireProjectile(player.sprite.rect.center[0], player.sprite.rect.center[1], "up")
                    if event.key == pygame.K_DOWN:
                        FireProjectile(player.sprite.rect.center[0], player.sprite.rect.center[1], "down")
                    if event.key == pygame.K_LEFT:
                        FireProjectile(player.sprite.rect.center[0], player.sprite.rect.center[1], "left")
                    if event.key == pygame.K_RIGHT:
                        FireProjectile(player.sprite.rect.center[0], player.sprite.rect.center[1], "right")

            # spawn enemy on timer
            if event.type == enemyTimer and game.IsRunning():
                enemyGroup.add(SpawnEnemy(SCREEN_WIDTH, SCREEN_HEIGHT))

        # End event loop

        # Logical updates
        if game.IsRunning():
            player.update()
            projectileGroup.update()
            enemyGroup.update(player)

            # Collisions
            # TODO: make this into functions

            # Check collision between projectiles and enemies, and delete both on collision.
            # groupcollide(group1, group2, dokill1, dokill2) -> Sprite_dict
            projectileCollision = pygame.sprite.groupcollide(projectileGroup, enemyGroup, True, True)

            # Check collision between enemy and player.
            # spritecollideany(sprite, group) -> Sprite
            playerCollision = pygame.sprite.spritecollideany(player.sprite, enemyGroup)
            # Deal damage to player on collision
            if playerCollision != None:
                player.sprite.TakeDamage(1)

                # check if player has died after collision
                if not player.sprite.IsAlive():
                    game.Update('death')
                    print(" player dead.")
                    print(f" 1. {game.currentState}")
                    
            # Graphical updates

            # Background
        screen.blit(backgroundSurface, (0, 0))

        # Entities
        projectileGroup.draw(screen)
        player.draw(screen)
        enemyGroup.draw(screen)

        # Text

        # Show start text
        if game.IsTitle():
            screen.blit(startText, startTextRect)

        # show pause text
        if game.IsPaused():
            screen.blit(pauseText, pauseTextRect)

        # If player dies
        if game.IsGameLose():
            screen.blit(deathText, deathTextRect)

        # Update display surface
        pygame.display.update()

        # Tick speed
        clock.tick(60)

main()
