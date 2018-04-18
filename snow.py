import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0, 255, 0)

class Snow(pygame.sprite.Sprite):

    def __init__(self, color, width, height, speed):
        super() .__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.image.net_colorkey(RED)
        self.width = width
        self.height = height
        self.color = speed

        pygame.draw.ellipse(self.image,color,[0,0,self.width,self.height])
        self.rect = self.image.get_rect()

    def moveBackward(self, speed):
        self.rect.y += selfspeed*speed / 20

    def changeSpeed(self, speed):
        self.speed = speed
