import pygame
from sys import exit
from player import Player

# Initialize pygame subsystems
pygame.init()

version = " v0.0.1"

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

# Colors

# Fonts

# Music

# Clock
clock = pygame.time.Clock()

# Functions

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

        # End event loop

        # Logical updates
        player.update()

        # Graphical updates

        # Background
        screen.blit(backgroundSurface, (0, 0))

        # Entities
        player.draw(screen)

        # Update display surface
        pygame.display.update()

        # Tick speed
        clock.tick(60)

main()
