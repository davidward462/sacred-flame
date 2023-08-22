import pygame

# class inherets from pygame sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self):

        # Initialize parent sprite class
        super().__init__()

        self.image = None
        self.rect = None
        
    # Update sprite logic
    def Update(self):
        self.destroy()

    # Destroy sprite
    def Destroy(self):
        condition = False
        if condition:
            self.kill()



