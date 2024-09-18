import pygame

class Cactus(pygame.sprite.Sprite):
    #create constant variables
    IMAGE = pygame.image.load('resources/cactus.png')
    STARTING_POSITION = (300,400)
    SIZE = (60, 60)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 1

    #cactus object constructor(creates cactus object)
    def __init__(self, starting_position: tuple, direction: str):
        # setup sprite
        super().__init__()
        self.image = Cactus.IMAGE

        self.rect = pygame.Rect((0, 0), Cactus.SIZE)
        self.rect.center = starting_position
        self.direction = direction

    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= Cactus.MOVE_DIST
            # checks if cactus is off the screen on the left, if true it resets the cactus position
            if self.rect.right <= 0:
                self.rect.centerx = Cactus.SCREEN_DIM[0] + (Cactus.SIZE[0] / 2)
        else:
            self.rect.centerx += Cactus.MOVE_DIST
            # if cactus moves off screen on the right then reset to the left
            if self.rect.left >= Cactus.SCREEN_DIM[0]:
                self.rect.centerx = -Cactus.SIZE[0]/2


