import pygame

# class inherets from pygame sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, startX, startY):

        # Initialize parent sprite class
        super().__init__()

        # Image and rectangle
        self.image = pygame.image.load('graphics/player-temp.png')
        self.rect = self.image.get_rect()
        self.rect.center = (startX, startY)

        self.velocityX = 0
        self.velocityY = 0
        self.speed = 6

        # Sounds

    def SetVelocity(self):
        self.velocityX = 0
        self.velocityY = 0

        # Get input and set velocity
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.velocityY -= 1
        if keys[pygame.K_s]:
            self.velocityY += 1
        if keys[pygame.K_a]:
            self.velocityX -= 1
        if keys[pygame.K_d]:
            self.velocityX += 1

        # Diagonal
        if self.velocityX != 0 and self.velocityY != 0:
            self.velocityX *= 0.7071
            self.velocityY *= 0.7071

    def Move(self):
        self.rect.x += (self.velocityX * self.speed)
        self.rect.y += (self.velocityY * self.speed)

    # Update sprite logic
    def update(self):
        self.SetVelocity()
        self.Move()
        self.delete()

    # Destroy sprite
    def delete(self):
        condition = False
        if condition:
            self.kill()



