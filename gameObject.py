import pygame

# class inherets from pygame sprite class
# This class represents some object which appears in the game world
class gameObject(pygame.sprite.Sprite):
    def __init__(self, screenWidth, screenHeight, position, imagePath):

        # Initialize parent sprite class
        super().__init__()

        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect(center = position)
        self.position = position