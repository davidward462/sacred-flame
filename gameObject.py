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

    # used to change size of flame object
    def UpdateScale(self, percent):
        # TODO: determine absolute factor somehow
        absoluteFactor = 5
        absolutePercent = percent * absoluteFactor
        scaledImage = pygame.transform.scale(self.image, (int(self.mySize[0]*absolutePercent), int(self.mySize[1]*absolutePercent)))
        self.image = scaledImage

        # Get the original bottom middle position
        original_bottom_middle = self.rect.midbottom

        # Update the image and rect
        self.image = scaledImage
        self.rect = self.image.get_rect()

        # Set the rect's bottom middle to the original position
        self.rect.midbottom = original_bottom_middle
