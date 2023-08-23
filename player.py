import pygame

# class inherets from pygame sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, startX, startY):

        # Initialize parent sprite class
        super().__init__()

        # Image
        self.image = pygame.image.load('graphics/player-temp.png')
        self.rect = self.image.get_rect(midbottom = (startX,startY))

        # Sounds
        
    # Update sprite logic
    def Update(self):
        self.destroy()

    # Destroy sprite
    def Destroy(self):
        condition = False
        if condition:
            self.kill()



