import pygame
from sys import exit
from random import randint
from player import Player
from projectile import Projectile
from enemy import Enemy

# Initialize pygame subsystems
pygame.init()

version = " v0.0.2"

# Set up window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
caption = f"Sacred Flame {version}"
pygame.display.set_caption(caption)

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

# Fonts

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
                # center is a tuple (x, y)
                if event.key == pygame.K_UP:
                    FireProjectile(player.sprite.rect.center[0], player.sprite.rect.center[1], "up")
                if event.key == pygame.K_DOWN:
                    FireProjectile(player.sprite.rect.center[0], player.sprite.rect.center[1], "down")
                if event.key == pygame.K_LEFT:
                    FireProjectile(player.sprite.rect.center[0], player.sprite.rect.center[1], "left")
                if event.key == pygame.K_RIGHT:
                    FireProjectile(player.sprite.rect.center[0], player.sprite.rect.center[1], "right")

            # spawn enemy on timer
            if event.type == enemyTimer:
                enemyGroup.add(SpawnEnemy(SCREEN_WIDTH, SCREEN_HEIGHT))

        # End event loop

        # Logical updates
        player.update()
        projectileGroup.update()
        enemyGroup.update(player)

        # Graphical updates

        # Background
        screen.blit(backgroundSurface, (0, 0))

        # Entities
        projectileGroup.draw(screen)
        player.draw(screen)
        enemyGroup.draw(screen)

        # Update display surface
        pygame.display.update()

        # Tick speed
        clock.tick(60)

main()
