import pygame

class Bee(pygame.sprite.Sprite):
    #create constant variables
    IMAGE = pygame.image.load('resources/killerbee.png')
    STARTING_POSITION = (300,350)
    SIZE = (60, 40)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 2

    #cactus object constructor(creates cactus object)
    def __init__(self, starting_position: tuple, direction: str):
        # setup sprite
        super().__init__()
        self.image = Bee.IMAGE

        self.rect = pygame.Rect((0, 0), Bee.SIZE)
        self.rect.center = Bee.STARTING_POSITION
        self.direction = direction

    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= Bee.MOVE_DIST
            # checks if cactus is off the screen on the left, if true it resets the cactus position
            if self.rect.right <= 0:
                self.rect.centerx = Bee.SCREEN_DIM[0] + (Bee.SIZE[0] / 2)
        else:
            self.rect.centerx += Bee.MOVE_DIST
            # if cactus moves off screen on the right then reset to the left
            if self.rect.left >= Bee.SCREEN_DIM[0]:
                self.rect.centerx = -Bee.SIZE[0]/2