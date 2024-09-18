import pygame

class Snake(pygame.sprite.Sprite):
    #Define constant values
    IMAGE = pygame.image.load('resources/snake.png')
    STARTING_POSITION = (300,150)
    SIZE = (60,40)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 1

    #constructor for snake object
    def __init__(self, starting_position:tuple, direction: str):
        #Sprite information
        super().__init__()
        self.image = Snake.IMAGE
        self.rect = pygame.Rect((0,0), Snake.SIZE)
        self.rect.center = starting_position
        self.direction = direction


    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= Snake.MOVE_DIST
            # checks if cactus is off the screen on the left, if true it resets the cactus position
            if self.rect.right <= 0:
                self.rect.centerx = Snake.SCREEN_DIM[0] + (Snake.SIZE[0] / 2)
        else:
            self.rect.centerx += Snake.MOVE_DIST
            # if cactus moves off screen on the right then reset to the left
            if self.rect.left >= Snake.SCREEN_DIM[0]:
                self.rect.centerx = -Snake.SIZE[0]/2


