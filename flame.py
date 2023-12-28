import pygame

# class inherets from pygame sprite class
# This class represents some object which appears in the game world
class Flame(pygame.sprite.Sprite):
    def __init__(self, posX, posY, imagePath):

        # Initialize parent sprite class
        super().__init__()

        self.posX = posX
        self.posY = posY
        self.imageOriginal = pygame.image.load(imagePath)
        self.image = self.imageOriginal
        self.imageSize = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.center = (self.posX, self.posY)
        self.size = 0

    # Change sprite size by argument 'change'
    def Resize(self, change):

        checkSizeX = self.size + change + self.imageSize[0]
        checkSizeY = self.size + change + self.imageSize[1]
        print(f"{checkSizeX}, {checkSizeY}")

        # change sprite size if new size won't be negative
        if checkSizeX >= 0 and checkSizeY >= 0:
            self.size += change
            xSize = self.imageSize[0] + round(self.size)
            ySize = self.imageSize[1] + round(self.size)
            self.image = pygame.transform.scale( self.imageOriginal, (xSize, ySize) )
            self.rect = self.image.get_rect( center = (self.posX, self.posY) )

    # Set sprite size to percent of whole given in argument 'percent'
    def SetSize(self, percent):
        currentSizeX = (percent) * self.imageSize[0]
        currentSizeY = (percent) * self.imageSize[1]

        self.image = pygame.transform.scale( self.imageOriginal, (currentSizeX, currentSizeY) )
        self.rect = self.image.get_rect( center = (self.posX, self.posY) )
