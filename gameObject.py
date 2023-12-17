import pygame

# class inherets from pygame sprite class
# This class represents some object which appears in the game world
class GameObject(pygame.sprite.Sprite):
    def __init__(self, posX, posY, imagePath):

        # Initialize parent sprite class
        super().__init__()

        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect(center = (posX, posY) )

        self.size = self.image.get_size()
        self.mySize = (10, 10)

    def UpdateScale(self, factor):
        percent = factor/100
        scaledImage = pygame.transform.scale(self.image, (int(self.mySize[0]*factor), int(self.mySize[1]*factor)))
        self.image = scaledImage