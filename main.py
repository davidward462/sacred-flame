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
def SpawnEnemy(screenDimensions, enemyImages):

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
    spawnPos = (ex, ey)
    enemyType = ChooseEnemyType(0.4)

    # create enemy at given position
    e = Enemy(screenDimensions, spawnPos, enemyType, enemyImages)

    return e

# delete old flame and create new one
def FlameReset(flamePosition, flameImage):
    flameGroup.empty()
    flameGroup.add( GameObject(flamePosition[0], flamePosition[1], flameImage) )

# Send game restart signal to game state machine
def GameRestart(flamePosition, flameImage):
    enemyGroup.empty()
    projectileGroup.empty()
    sparkGroup.empty()
    player.sprite.Restart()
    FlameReset(flamePosition, flameImage)
    game.Update('r')

# Send game start signal to game state machine
def GameStart():
    game.Update('space')


# Create projectile at position of player and give direction
# Only fire if delay condition is passed
def FireProjectile(screenDimensions, posX, posY, direction, lastFireTime, projectileImage):

    fireDelay = 500

    # get current time
    currentTime = pygame.time.get_ticks()

    # difference between now and last shot
    dt = currentTime - lastFireTime

    if dt > fireDelay:

        p = Projectile(screenDimensions, posX, posY, projectileImage)
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
#   inFont: font of text
#   screen: screen on which to draw the text
def DrawText(input, posX, posY, font, screen):
    textIn = str(input)
    text = font.render(textIn, True, 'white', 'black') 
    textRect = text.get_rect()
    textRect.center = (posX, posY)
    screen.blit(text, textRect)

# Shutdown pygame and exit program.
def QuitGame():
    pygame.quit()
    exit()

def main():

    # Default window dimensions
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 608

    # get user display info
    USER_DISPLAY = pygame.display.Info()  

    # make sure window is not larger than user's display
    currentScreenWidth = min(SCREEN_WIDTH, USER_DISPLAY.current_w)
    currentScreenHeight = min(SCREEN_HEIGHT, USER_DISPLAY.current_h)

    # dimension tuple for passing to functions
    screenDimensions = (currentScreenWidth, currentScreenHeight)

    # Display surface
    screen = pygame.display.set_mode((currentScreenWidth, currentScreenHeight))
    caption = f"Sacred Flame"
    pygame.display.set_caption(caption)

    screenWidthCenter = currentScreenWidth/2
    screenHeightCenter = currentScreenHeight/2

    # Surfaces

    # Game object variables

    # place pillar in the center of the screen
    pillarPosX = screenWidthCenter
    pillarPosY = screenHeightCenter

    # place flame above pillar
    flamePosX = pillarPosX
    flamePosY = pillarPosY - 65
    flamePosition = (flamePosX, flamePosY)

    # player start position
    playerSpawnPosition = (screenWidthCenter, screenHeightCenter + 200)

    # Graphics

    tilesize = 64

    altarImage = 'graphics/flame-altar.png'
    pillarImage = 'graphics/pillar.png'
    flameImage = 'graphics/flame.png'
    playerImage = 'graphics/player-blue.png'
    enemyBasicImage = 'graphics/serpent-hybrid.png'
    enemyRedImage = 'graphics/demon.png'
    sparkImage = 'graphics/spark.png'
    projectileImage = 'graphics/magic.png'
    floorTile = 'graphics/floor-wide.png'

    enemyImages = (enemyBasicImage, enemyRedImage)

    # background
    backgroundSurface = pygame.image.load(floorTile).convert_alpha()

    # Add entities to groups
    player.add( Player(screenDimensions, playerSpawnPosition, playerImage) )
    # objectGroup.add( GameObject(pillarPosX, pillarPosY, pillarImage) )
    objectGroup.add( GameObject(pillarPosX, pillarPosY, altarImage) )
    flameGroup.add( GameObject(flamePosX, flamePosY, flameImage) )

    # Fonts

    # TODO: determine final font style
    defaultFont = pygame.font.SysFont('freesansbold', 32)

    # Start of game font
    # startFont = pygame.font.SysFont('freesansbold', 32)
    startText = defaultFont.render("Press SPACE to begin", True, 'white', 'black') 
    startTextRect = startText.get_rect()
    startTextRect.center = (currentScreenWidth / 2, currentScreenHeight / 2)

    # Pause screen font
    # pauseFont = pygame.font.SysFont('freesansbold', 32)
    pauseText = defaultFont.render("Game paused", True, 'white', 'black') 
    pauseTextRect = pauseText.get_rect()
    pauseTextRect.center = (currentScreenWidth / 2, currentScreenHeight / 2)

    # Player death font
    # deathFont = pygame.font.SysFont('freesansbold', 32)
    deathText = defaultFont.render("You Died", True, 'white', 'black') 
    deathTextRect = deathText.get_rect()
    deathTextRect.center = (currentScreenWidth / 2, currentScreenHeight / 2)

    # Flame out font
    # flameOutFont = pygame.font.SysFont('freesansbold', 32)
    flameOutText = defaultFont.render("The Flame went out", True, 'white', 'black') 
    flameOutTextRect = flameOutText.get_rect()
    flameOutTextRect.center = (currentScreenWidth / 2, currentScreenHeight / 2)

    # Music

    # Clock and timers
    clock = pygame.time.Clock()
    timeFactor = 100
    flameTimerMax = 60 #TODO: determine time limit

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
                        GameRestart(flamePosition, flameImage)
                
                # get player input
                if game.IsRunning():
                    if event.key == pygame.K_UP:
                        lastFireTime = FireProjectile(screenDimensions, player.sprite.rect.center[0], player.sprite.rect.center[1], "up", lastFireTime, projectileImage)
                    if event.key == pygame.K_DOWN:
                        lastFireTime = FireProjectile(screenDimensions, player.sprite.rect.center[0], player.sprite.rect.center[1], "down", lastFireTime, projectileImage)
                    if event.key == pygame.K_LEFT:
                        lastFireTime = FireProjectile(screenDimensions, player.sprite.rect.center[0], player.sprite.rect.center[1], "left", lastFireTime, projectileImage)
                    if event.key == pygame.K_RIGHT:
                        lastFireTime = FireProjectile(screenDimensions, player.sprite.rect.center[0], player.sprite.rect.center[1], "right", lastFireTime, projectileImage)

            # spawn enemy on timer
            if event.type == enemyTimer and game.IsRunning():
                enemyGroup.add(SpawnEnemy(screenDimensions, enemyImages))

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
                    sparkGroup.add( Spark(spawnX, spawnY, sparkImage) )
            
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

        # tile the background
        for widthPos in range(0,currentScreenWidth, tilesize):
            for heightPos in range(0, currentScreenHeight, tilesize):
                screen.blit(backgroundSurface, (widthPos+1, heightPos))


        # Entities
        projectileGroup.draw(screen)
        player.draw(screen)
        enemyGroup.draw(screen)
        objectGroup.draw(screen)
        # flameGroup.draw(screen)
        sparkGroup.draw(screen)

        # update scale for flame
        flameFraction = flameTimeCurrent / flameTimerMax
        flameGroup.sprite.UpdateScale( flameFraction )

        # whole number percent
        flamePercent = int(flameFraction * 100)

        # Text

        # show flame percent on screen
        # TODO:  remove this in final version
        drawThis = str(flamePercent) + "%"
        DrawText(drawThis, 100, 50, defaultFont, screen)

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
