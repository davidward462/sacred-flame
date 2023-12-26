import pygame

# class inherets from pygame sprite class
# This class represents some object which appears in the game world
class Flame(pygame.sprite.Sprite):
    def __init__(self, posX, posY, imagePath):

        # Initialize parent sprite class
        super().__init__()

        self.growth_rate = 1

        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect(center = (posX, posY) )

        self.size = self.image.get_size()
        self.mySize = (10, 10)

        self.original_image = self.image

    def update(self):
        self.image_scale += self.growth_rate
        self.image = pygame.transform.scale(
            self.original_image, (self.image_scale, self.image_scale))

        self.rect = self.image.get_rect(center = self.rect.center)