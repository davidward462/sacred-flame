import pygame

# class inherets from pygame sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, screenWidth, screenHeight):

        # Initialize parent sprite class
        super().__init__()

        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.image = None
        self.rect = None
        
    # Update sprite logic
    def update(self):
        self.destroy()

    # Destroy sprite
    def delete(self):
        condition = False
        if condition:
            self.kill()



