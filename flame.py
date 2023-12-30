import pygame

# class inherets from pygame sprite class
# This class represents some object which appears in the game world
class Flame(pygame.sprite.Sprite):
    def __init__(self, posX, posY, imagePathList):

        # Initialize parent sprite class
        super().__init__()

        self.posX = posX
        self.posY = posY
        self.imageOriginal = pygame.image.load(imagePathList[0])
        self.image = self.imageOriginal
        self.imageSize = self.image.get_size()
        # self.rect = self.image.get_rect()
        # self.rect.center = (self.posX, self.posY)
        self.size = 0

        self.frameList = []
        
        frameCount = len(imagePathList)

        for i in range(frameCount):
            self.frameList.append( pygame.image.load(imagePathList[i]) )

        self.animationIndex = 0

        self.image = self.frameList[self.animationIndex] 
        self.rect = self.image.get_rect(center = (posX, posY) )

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

        self.image = pygame.transform.scale( self.frameList[ int(self.animationIndex) ], (currentSizeX, currentSizeY) )
        self.rect = self.image.get_rect( center = (self.posX, self.posY) )


    def Animate(self):
        self.animationIndex += 0.1
        if self.animationIndex >= len(self.frameList):
            self.animationIndex = 0

    def update(self):
        self.Animate()
