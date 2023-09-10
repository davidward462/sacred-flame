import pygame

# class inherets from pygame sprite class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, screenWidth, screenHeight, position, enemyType):

        # Initialize parent sprite class
        super().__init__()

        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.image = pygame.image.load('graphics/entity.png')
        self.rect = self.image.get_rect(center = position)
        self.position = pygame.math.Vector2(position) # position of enemy is a vector type
        
        self.speed = 1

    def MoveTowardsPlayer(self, player):
        playerPosition = player.sprite.rect.center
        direction = playerPosition - self.position
        velocity = direction.normalize() * self.speed

        self.position += velocity
        self.rect.center = self.position

    def Move(self):
        cx = self.rect.x
        cy = self.rect.y

        # Move enemy

        self.rect.x = cx
        self.rect.y = cy
        
    # Update sprite logic
    def update(self, player):
        self.MoveTowardsPlayer(player)
        self.delete()

    # Destroy sprite
    def delete(self):
        condition = False
        if condition:
            self.kill()



