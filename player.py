import pygame

# class inherets from pygame sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, startX, startY):

        # Initialize parent sprite class
        super().__init__()

        # Image and rectangle
        self.image = pygame.image.load('graphics/player-temp.png')
        self.rect = self.image.get_rect(midbottom = (startX,startY))

        self.vx = 0
        self.vy = 0
        self.speed = 6

        # Sounds

    def SetVelocity(self):
        self.vx = 0
        self.vy = 0

        # Get input and set velocity
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.vy -= 1
        if keys[pygame.K_s]:
            self.vy += 1
        if keys[pygame.K_a]:
            self.vx -= 1
        if keys[pygame.K_d]:
            self.vx += 1

        # Diagonal
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def Move(self):
        self.rect.x += (self.vx * self.speed)
        self.rect.y += (self.vy * self.speed)

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



