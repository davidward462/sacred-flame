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

        # Direction player should move
        self.hDir = 0
        self.vDir = 0

        # Max speed of player in any direction
        self.maxSpeed = 3.5

        # Current speed
        self.speed = 1

        # Image and rectangle
        self.image = pygame.image.load('graphics/player-temp.png')
        self.rect = self.image.get_rect(midbottom = (startX,startY))

        # Sounds

    def GetInput(self):
        keys = pygame.key.get_pressed()
        self.moveUp = keys[pygame.K_w]
        self.moveLeft = keys[pygame.K_a]
        self.moveDown = keys[pygame.K_s]
        self.moveRight = keys[pygame.K_d]

    def SetHorizontalDir(self):
        hDir = 0
        if self.moveLeft:
            hDir -= 1
        if self.moveRight:
            hDir += 1

        self.hDir = hDir

    def SetVerticalDir(self):
        vDir = 0
        if self.moveUp:
            vDir -= 1
        if self.moveDown:
            vDir += 1

        self.vDir = vDir

    def CalcSpeed(self):
        a = self.hDir
        b = self.vDir

        hypoteneuse = (a*a + b*b)**0.5

        if hypoteneuse != 0:
            self.speed = 1/hypoteneuse
        else:
            self.speed = 0
        
    # Move player
    def MovePlayer(self):
        cx = self.rect.x
        cy = self.rect.y

        cx += self.hDir * self.maxSpeed * self.speed
        cy += self.vDir * self.maxSpeed * self.speed

        self.rect.x = cx
        self.rect.y = cy
        
    # Update sprite logic
    def update(self):
        self.GetInput()
        self.SetHorizontalDir()
        self.SetVerticalDir()
        self.CalcSpeed()
        self.MovePlayer()
        self.delete()

    # Destroy sprite
    def delete(self):
        condition = False
        if condition:
            self.kill()



