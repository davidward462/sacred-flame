import pygame

# class inherets from pygame sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, screenDimensions, spawnPosition, playerImageSet):

        # Initialize parent sprite class
        super().__init__()

        self.screenWidth = screenDimensions[0]
        self.screenHeight = screenDimensions[1]

        self.startX = spawnPosition[0]
        self.startY = spawnPosition[1]

        # Image and rectangle
        self.imageAlive = pygame.image.load(playerImageSet[0])
        self.imageDead = pygame.image.load(playerImageSet[1])
        self.image = self.imageAlive
        self.rect = self.image.get_rect()
        self.rect.center = (self.startX, self.startY)

        self.velocityX = 0
        self.velocityY = 0
        self.speed = 5
    
        self.maxHealth = 1
        self.health = self.maxHealth
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

    def Restart(self):
        self.health = self.maxHealth
        self.isAlive = True
        self.rect.x = self.startX
        self.rect.y = self.startY

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
        if self.health > 0:
            self.isAlive = True
        else:
            self.isAlive = False

    def IsAlive(self):
        return self.isAlive

    def SetSprite(self):
        if self.isAlive:
            self.image = self.imageAlive
        else:
            self.image = self.imageDead

    # Update sprite logic
    def update(self):
        self.SetVelocity()
        self.Move()
        self.CheckHealth()
        self.SetSprite()
        self.delete()

    # Destroy sprite
    def delete(self):
        condition = False
        if condition:
            self.kill()



