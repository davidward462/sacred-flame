import pygame

# class inherets from pygame sprite class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, screenWidth, screenHeight, startX, startY, enemyType):

        # Initialize parent sprite class
        super().__init__()

        self.startX = startX
        self.startY = startY
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.image = pygame.image.load('graphics/entity.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.startX, self.startY)

    def Move(self):
        cx = self.rect.x
        cy = self.rect.y

        # Move enemy

        self.rect.x = cx
        self.rect.y = cy
        
    # Update sprite logic
    def update(self):
        self.delete()

    # Destroy sprite
    def delete(self):
        condition = False
        if condition:
            self.kill()



