import pygame

# class inherets from pygame sprite class
# This class represents some object which appears in the game world
class Spark(pygame.sprite.Sprite):
    def __init__(self, posX, posY, imagePath):

        # Initialize parent sprite class
        super().__init__()

        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect(center = (posX, posY) )

