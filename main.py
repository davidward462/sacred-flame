import pygame
from sys import exit
import math
import random
from game import Game
from player import Player
from projectile import Projectile
from enemy import Enemy
from gameObject import GameObject
from spark import Spark

# Initialize pygame subsystems
pygame.init()

# Game state object
game = Game()

# Groups
# Player group
player = pygame.sprite.GroupSingle()

# Projectile group
projectileGroup = pygame.sprite.Group()

# Enemy group
enemyGroup = pygame.sprite.Group()

# Object group
objectGroup = pygame.sprite.Group()

# Flame group
flameGroup = pygame.sprite.GroupSingle()

# Spark group
sparkGroup = pygame.sprite.Group()

# Functions

# return an random position tuple within the bounds provided
def RandomCoordinates(width, height):
    x = random.randint(0, width)
    y = random.randint(0, height)
    return (x, y)

# Euclidian distance 
def DistanceBetweenPoints(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    c = math.sqrt( a**2 + b**2 )
    return c

def ChooseEnemyType(chance):
    randomChoice = random.random()
    if randomChoice > chance:
        return "basic"
    else:
        return "red"

# spawn enemy on the given radius of the circle
def SpawnEnemy(screenDimensions, playerX, playerY):

    screenWidth = screenDimensions[0]
    screenHeight = screenDimensions[1]

    minDistance = screenWidth/2 + 100
    maxDistance = minDistance + 100
    
    # random angle
    angle = 2 * math.pi * random.random()

    # random values within bounds
    x = random.randint(minDistance, maxDistance)
    y = random.randint(minDistance, maxDistance)

    # calculate point based on given angle, and shift to be based on center of screen
    ex = x * math.cos(angle) + screenWidth/2
    ey = y * math.sin(angle) + screenHeight/2

    # set spawn tuple
    spawn = (ex, ey)
    enemyType = ChooseEnemyType(0.3)

    # create enemy at given position
    e = Enemy(screenWidth, screenHeight, spawn, enemyType)

    return e

# Send game restart signal to game state machine
def GameRestart():
    enemyGroup.empty()
    projectileGroup.empty()
    sparkGroup.empty()
    player.sprite.Restart()
    game.Update('r')

# Send game start signal to game state machine
def GameStart():
    game.Update('space')


# Create projectile at position of player and give direction
# Only fire if delay condition is passed
def FireProjectile(screenDimensions, posX, posY, direction, lastFireTime):

    screenWidth = screenDimensions[0]
    screenHeight = screenDimensions[1]
    fireDelay = 500

    # get current time
    currentTime = pygame.time.get_ticks()

    # difference between now and last shot
    dt = currentTime - lastFireTime

    if dt > fireDelay:

        p = Projectile(screenWidth, screenHeight, posX, posY)
        if direction == "up":
            p.vy = -1
        if direction == "down":
            p.vy = 1
        if direction == "left":
            p.vx = -1
        if direction == "right":
            p.vx = 1
        projectileGroup.add(p)

        return currentTime
    
    else:
        # No projectile created
        return lastFireTime

# Draw text to screen. 
# Params: 
#   input: data to draw, 
#   posX/posY: postion of text on screen
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

    # Default window dimensions
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768

    # get user display info
    USER_DISPLAY = pygame.display.Info()  

    # make sure window is not larger than user's display
    currentScreenWidth = min(SCREEN_WIDTH, USER_DISPLAY.current_w)
    currentScreenHeight = min(SCREEN_HEIGHT, USER_DISPLAY.current_h)

    # dimension tuple for passing to functions
    screenDimensions = (currentScreenWidth, currentScreenHeight)
    print(f"running at {screenDimensions[0]} x {screenDimensions[1]}")

    
    version = " v0.6.0"

    centerX = SCREEN_WIDTH/2
    centerY = SCREEN_HEIGHT/2

    # Display surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    caption = f"Sacred Flame {version}"
    pygame.display.set_caption(caption)

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Surfaces
    # backgroundSurface = pygame.image.load('graphics/bg-blue-1024.png').convert_alpha()

    # background
    screen.fill('grey32')

    # Game object variables

    # place pillar in the center of the screen
    pillarPosX = currentScreenWidth/2
    pillarPosY = currentScreenHeight/2

    # place flame above pillar
    flamePosX = pillarPosX
    flamePosY = pillarPosY - 65


    # Add entities to groups
    player.add(Player(currentScreenWidth, currentScreenHeight))
    objectGroup.add( GameObject(pillarPosX, pillarPosY, 'graphics/pillar-temp.png') )
    flameGroup.add( GameObject(flamePosX, flamePosY, 'graphics/flame-temp.png') )

    # Fonts

    # TODO: determine final font style
    defaultFont = pygame.font.SysFont('freesansbold', 32)

    # Start of game font
    # startFont = pygame.font.SysFont('freesansbold', 32)
    startText = defaultFont.render("Press SPACE to begin", True, white, black) 
    startTextRect = startText.get_rect()
    startTextRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Pause screen font
    # pauseFont = pygame.font.SysFont('freesansbold', 32)
    pauseText = defaultFont.render("Game paused", True, white, black) 
    pauseTextRect = pauseText.get_rect()
    pauseTextRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Player death font
    # deathFont = pygame.font.SysFont('freesansbold', 32)
    deathText = defaultFont.render("You Died", True, white, black) 
    deathTextRect = deathText.get_rect()
    deathTextRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Flame out font
    # flameOutFont = pygame.font.SysFont('freesansbold', 32)
    flameOutText = defaultFont.render("The Flame went out", True, white, black) 
    flameOutTextRect = flameOutText.get_rect()
    flameOutTextRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Music

    # Clock and timers
    clock = pygame.time.Clock()
    timeFactor = 100
    flameTimerMax = 70

    # Enemy spawning timer
    enemyTimer = pygame.USEREVENT + 1
    enemyTimerRate = 1500
    pygame.time.set_timer(enemyTimer, enemyTimerRate)

    # Flame timer
    flameTimer = pygame.USEREVENT + 2
    flameTimerRate = 500
    pygame.time.set_timer(flameTimer, flameTimerRate)

    # projectile cooldown timer
    projectileCooldownTimer = pygame.USEREVENT + 3
    projectileCooldownTimerRate = 2000
    pygame.time.set_timer(projectileCooldownTimer, projectileCooldownTimerRate)

    # Timer functions
    startTime = int(pygame.time.get_ticks() / timeFactor)
    lastFireTime = startTime
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
                if event.key == pygame.K_q:
                    if game.currentState != 'running':
                    # Only accept close escape game input if game is not in the running state
                        QuitGame()
                
                if event.key == pygame.K_SPACE:
                    if game.currentState == 'title':
                        GameStart()
                
                if event.key == pygame.K_ESCAPE:
                    # pause game
                    game.Update('esc')
                
                if event.key == pygame.K_r:
                    if game.currentState == 'playerDead' or game.currentState == 'darkness':
                        flameTimeCurrent = flameTimerMax
                        GameRestart()
                
                # get player input
                if game.IsRunning():
                    if event.key == pygame.K_UP:
                        lastFireTime = FireProjectile(screenDimensions, player.sprite.rect.center[0], player.sprite.rect.center[1], "up", lastFireTime)
                    if event.key == pygame.K_DOWN:
                        lastFireTime = FireProjectile(screenDimensions, player.sprite.rect.center[0], player.sprite.rect.center[1], "down", lastFireTime)
                    if event.key == pygame.K_LEFT:
                        lastFireTime = FireProjectile(screenDimensions, player.sprite.rect.center[0], player.sprite.rect.center[1], "left", lastFireTime)
                    if event.key == pygame.K_RIGHT:
                        lastFireTime = FireProjectile(screenDimensions, player.sprite.rect.center[0], player.sprite.rect.center[1], "right", lastFireTime)

            # spawn enemy on timer
            if event.type == enemyTimer and game.IsRunning():
                
                playerX = player.sprite.rect.center[0]
                playerY = player.sprite.rect.center[1]

                enemyGroup.add(SpawnEnemy(screenDimensions, playerX, playerY))

            # Decrement flame timer on tick
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
                game.Update('flameOut')

            # Collisions
            # TODO: make this into functions

            # Check collision between projectiles and enemies, and delete both on collision.
            # groupcollide(group1, group2, dokill1, dokill2) -> Sprite_dict
            projectileCollision = pygame.sprite.groupcollide(enemyGroup, projectileGroup,  True, True)

            # loop through sprites in returned sprite dict
            for sprite in projectileCollision:
                # get type
                enemyType = sprite.GetType()
                if enemyType == 'red':
                    # Get position of enemy the bullet collided with
                    spawnX = sprite.position[0]
                    spawnY = sprite.position[1]
                    # create spark object
                    sparkGroup.add( Spark(spawnX, spawnY, 'graphics/spark-temp.png') )
            
            # Check collision between enemy and player.
            # spritecollideany(sprite, group) -> Sprite
            playerCollision = pygame.sprite.spritecollideany(player.sprite, enemyGroup)
            # Deal damage to player on collision
            if playerCollision != None:
                player.sprite.TakeDamage(1)

                # check if player has died after collision
                if not player.sprite.IsAlive():
                    game.Update('death')

            # check collision between player and spark
            sparkCollision = pygame.sprite.spritecollide(player.sprite, sparkGroup, True)
            if sparkCollision:
                flameTimeCurrent += 5

                # keep flame timer below or equal to maximum
                if flameTimeCurrent > flameTimerMax:
                    flameTimeCurrent = flameTimerMax

                    
            # Graphical updates

        # Background
        screen.fill('grey32')
        # screen.blit(backgroundSurface, (0, 0))

        # Entities
        projectileGroup.draw(screen)
        player.draw(screen)
        enemyGroup.draw(screen)
        objectGroup.draw(screen)
        flameGroup.draw(screen)
        sparkGroup.draw(screen)

        # update scale for flame
        flamePercent = flameTimeCurrent / flameTimerMax
        flameGroup.sprite.UpdateScale( flamePercent )

        # Text

        # If on the title screen
        if game.IsTitle():
            screen.blit(startText, startTextRect)

        # If game is paused
        if game.IsPaused():
            screen.blit(pauseText, pauseTextRect)

        # If player dies
        if game.PlayerIsDead():
            screen.blit(deathText, deathTextRect)

        # If flame goes out
        if game.IsDarkness():
            screen.blit(flameOutText, flameOutTextRect)

        # Update display surface
        pygame.display.update()

        # Tick speed
        clock.tick(60)

main()
