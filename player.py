import pygame

# class inherets from pygame sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, startX, startY):

        # Initialize parent sprite class
        super().__init__()

        # instance variables
        self.moveUp = False
        self.moveLeft = False
        self.moveDown = False
        self.moveRight = False

        # Intended speed of player
        self.maxSpeed = 4

        self.speed = 1

        # Image
        self.image = pygame.image.load('graphics/player-temp.png')
        self.rect = self.image.get_rect(midbottom = (startX,startY))

        # Sounds

    def GetInput(self):
        keys = pygame.key.get_pressed()
        self.moveUp = keys[pygame.K_UP]
        self.moveLeft = keys[pygame.K_LEFT]
        self.moveDown = keys[pygame.K_DOWN]
        self.moveRight = keys[pygame.K_RIGHT]

    # Move player
    def MovePlayer(self):
        cx = self.rect.x
        cy = self.rect.y

        if self.moveUp:
            cy = cy - self.maxSpeed
        if self.moveLeft:
            cx = cx - self.maxSpeed
        if self.moveDown:
            cy = cy + self.maxSpeed
        if self.moveRight:
            cx = cx + self.maxSpeed

        self.rect.x = cx
        self.rect.y = cy
        
    # Update sprite logic
    def update(self):
        self.GetInput()
        self.MovePlayer()
        self.delete()

    # Destroy sprite
    def delete(self):
        condition = False
        if condition:
            self.kill()



