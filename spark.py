import pygame

# class inherets from pygame sprite class
# This class represents some object which appears in the game world
class Spark(pygame.sprite.Sprite):
    def __init__(self, posX, posY, imagePathList):

        # Initialize parent sprite class
        super().__init__()

        self.frameList = []
        
        frameCount = len(imagePathList)

        for i in range(frameCount):
            self.frameList.append( pygame.image.load(imagePathList[i]) )

        self.animationIndex = 0

        self.image = self.frameList[self.animationIndex] 
        self.rect = self.image.get_rect(center = (posX, posY) )

    def Animate(self):
        self.animationIndex += 0.1
        if self.animationIndex >= len(self.frameList):
            self.animationIndex = 0
        self.image = self.frameList[int(self.animationIndex)]

    def update(self):
        self.Animate()
