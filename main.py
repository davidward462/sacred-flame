import pygame
from sys import exit
from random import randint
from game import Game
from player import Player
from projectile import Projectile
from enemy import Enemy
from gameObject import GameObject

# Initialize pygame subsystems
pygame.init()

version = " v0.0.8"

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

'''
pillarImage = pygame.image.load('graphics/pillar-temp.png')
pillarRect = pillarImage.get_rect()
pillarRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
'''

# Game object variables
pillarPosX = SCREEN_WIDTH/2
pillarPosY = SCREEN_HEIGHT/2

flamePosX = pillarPosX
flamePosY = pillarPosY - 50

flameTimerMax = 5

# Player variables

# Groups
# Player group
player = pygame.sprite.GroupSingle()
player.add(Player(SCREEN_WIDTH, SCREEN_HEIGHT))

# Projectile group
projectileGroup = pygame.sprite.Group()

# Enemy group
enemyGroup = pygame.sprite.Group()

# Object group
objectGroup = pygame.sprite.Group()
objectGroup.add( GameObject(pillarPosX, pillarPosY, 'graphics/pillar-temp.png') )

flameGroup = pygame.sprite.GroupSingle()
flameGroup.add( GameObject(flamePosX, flamePosY, 'graphics/flame-temp.png') )

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

defaultFont = pygame.font.SysFont('freesansbold', 32)

# Music

# Clock and timers
clock = pygame.time.Clock()
timeFactor = 100

# Enemy spawning timer
enemyTimer = pygame.USEREVENT + 1
enemyTimerRate = 3000
pygame.time.set_timer(enemyTimer, enemyTimerRate)

# Flame timer
flameTimer = pygame.USEREVENT + 2
flameTimerRate = 1000
pygame.time.set_timer(flameTimer, flameTimerRate)

# Functions
def SpawnEnemy(SCREEN_WIDTH, SCREEN_HEIGHT):
    
    spawnX = randint(0, SCREEN_WIDTH)
    spawnY = randint(0, SCREEN_HEIGHT)
    spawn = (spawnX, spawnY)

    e = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT, spawn, "basic")
    return e

def GameRestart():
    enemyGroup.empty()
    projectileGroup.empty()
    player.sprite.Restart()
    game.Update('rInput')

def GameStart():
    game.Update('spaceInput')


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

def DrawText(input, posX, posY):
    textIn = str(input)
    text = defaultFont.render(textIn, True, white, black) 
    textRect = text.get_rect()
    textRect.center = (posX, posY)
    screen.blit(text, textRect)

# Shutdown pygame and exit program.
def QuitGame():
    pygame.quit()
    exit()

def main():

    startTime = int(pygame.time.get_ticks() / timeFactor)
    flameTimeCurrent = flameTimerMax

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
                    if game.currentState != 'running':
                    # Only accept close escape game input if game is not in the running state
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

            if event.type == flameTimer and game.IsRunning():
                flameTimeCurrent -= 1

        # End event loop

        # Logical updates
        if game.IsRunning():
            currentTime = int(pygame.time.get_ticks() / timeFactor) - startTime
            player.update()
            projectileGroup.update()
            enemyGroup.update(player)

            # Check flame timer
            if flameTimeCurrent <= 0:
                flameTimeCurrent = flameTimerMax
                game.Update('death')

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
                    
            # Graphical updates

        # Background
        screen.blit(backgroundSurface, (0, 0))

        # Entities
        projectileGroup.draw(screen)
        player.draw(screen)
        enemyGroup.draw(screen)
        objectGroup.draw(screen)
        flameGroup.draw(screen)

        # update scale for flame
        # TODO: maybe make flame a single group
        for obj in flameGroup.sprites():
            obj.UpdateScale(flameTimeCurrent)

        DrawText(currentTime, 100, 100)
        DrawText(flameTimeCurrent, 100, 200)

        # Text

        # If on the title screen
        if game.IsTitle():
            screen.blit(startText, startTextRect)

        # If game is paused
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
