import pygame

# class inherets from pygame sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, screenWidth, screenHeight):

        # Initialize parent sprite class
        super().__init__()

        self.startX = screenWidth/2
        self.startY = screenHeight/2
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        # Image and rectangle
        self.image = pygame.image.load('graphics/player-temp.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.startX, self.startY)

        self.velocityX = 0
        self.velocityY = 0
        self.speed = 6

        self.health = 1
        self.isAlive = True

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
        cx = self.rect.x
        cy = self.rect.y

        cx += (self.velocityX * self.speed)
        cy += (self.velocityY * self.speed)

        # Bound player within screen
        cx = max( 0, min(cx, self.screenWidth - self.rect.width) )
        cy = max( 0, min(cy, self.screenHeight - self.rect.height) )

        self.rect.x = cx
        self.rect.y = cy

    # Reduce player health by the specified argument 'damage'
    def TakeDamage(self, damage):
        self.health = self.health - damage

    def GetHealth(self):
        return self.health

    # Set health to specified argument
    def SetHealth(self, value):
        self.health = value

    # Increment health by specified argument 
    def AddHealth(self, value):
        self.health = self.health + value

    # Set player to dead if health is zero or less
    def CheckHealth(self):
        if self.health < 1:
            self.isAlive = False

    def IsAlive(self):
        return self.isAlive

    # Update sprite logic
    def update(self):
        self.SetVelocity()
        self.Move()
        self.CheckHealth()
        self.delete()

    # Destroy sprite
    def delete(self):
        condition = False
        if condition:
            self.kill()



