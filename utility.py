import pygame
from math import sqrt

# return an random position tuple within the bounds provided
def RandomCoordinates(width, height):
    x = randint(0, width)
    y = randint(0, height)
    return (x, y)

def DistanceBetweenPoints(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    c = sqrt( a**2 + b**2 )
    return c

# Send game restart signal to game state machine
def GameRestart():
    enemyGroup.empty()
    projectileGroup.empty()
    player.sprite.Restart()
    game.Update('rInput')

# Send game start signal to game state machine
def GameStart():
    game.Update('spaceInput')


# Shutdown pygame and exit program.
def QuitGame():
    pygame.quit()
    exit()
