import pygame
from sys import exit
import sprite

# Initialize pygame subsystems
pygame.init()

# Set up window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
caption = "Sacred Flame"
pygame.display.set_caption(caption)

# Surfaces
backgroundSurface = None

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

        # Graphical updates

        # Update display surface
        pygame.display.update()

        # Tick speed
        clock.tick(60)

main()
