import pygame

# class inherets from pygame sprite class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, screenDimensions, startX, startY):

        # Initialize parent sprite class
        super().__init__()

        self.startX = startX
        self.startY = startY
        self.screenWidth = screenDimensions[0]
        self.screenHeight = screenDimensions[1]

        self.image = pygame.image.load('graphics/temp/projectile-temp.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.startX, self.startY)

        self.insideScreen = True

        self.vx = 0
        self.vy = 0
        self.speed = 10

    # Move projectile in particular direction
    def Move(self):     
        cx = self.rect.x
        cy = self.rect.y

        cx += self.vx * self.speed
        cy += self.vy * self.speed

        self.rect.x = cx
        self.rect.y = cy

    # Check if projectile is inside the bounds of the screen
    def IsInsideScreen(self):
        cx = self.rect.x
        cy = self.rect.y
        if cx < 0 or cx > self.screenWidth or cy < 0 or cy > self.screenHeight:
            self.insideScreen = False

    def SetSpeed(self, speed):
        self.speed = speed

    def GetSpeed(self):
        return self.speed

    # Update sprite logic
    def update(self):
        self.Move()
        self.IsInsideScreen()
        self.delete()

    # Destroy sprite
    def delete(self):
        if not self.insideScreen:
            self.kill()



