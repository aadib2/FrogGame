from snake import Snake
import pygame

class Frog(pygame.sprite.Sprite):
    #Define the constant values
    STARTING_POSITION = (300, 490)
    SIZE = (20,10)
    IMAGE = pygame.image.load('resources/Frog.png')
    MOVE_DIST = 10
    SCREEN_DIM = 600,500

     #constructor for frog object
    def __init__(self):
        #sprite setup
        super().__init__()
        self.image = Frog.IMAGE
        #frog rectangle
        self.rect = pygame.Rect((0,0),Frog.SIZE)
        self.rect.center = Frog.STARTING_POSITION
        self.lives=3

    def move_up(self):
        if self.rect.top>=20:
           self.rect.centery -= Frog.MOVE_DIST

    def move_down(self):
       if self.rect.bottom <= Frog.SCREEN_DIM[1] - 20:
           self.rect.centery += Frog.MOVE_DIST
    def move_left(self):
        if self.rect.left >= 20:
            self.rect.centerx -= Frog.MOVE_DIST

    def move_right(self):
        if self.rect.right <= Frog.SCREEN_DIM[0] - 20:
            self.rect.centerx += Frog.MOVE_DIST

    def reset_position(self):
        self.rect.center = Frog.STARTING_POSITION
        self.lives-=1

    def move_on_snake(self, snake: Snake):
        # Log moving right
        if snake.direction == 'Right':
            self.rect.centerx += Snake.MOVE_DIST
            # Frog has moved off screen
            if self.rect.left >= Snake.SCREEN_DIM[0]:
                diff = snake.rect.right - self.rect.centerx
                self.rect.centerx = Frog.SCREEN_DIM[0]/2
                self.rect.centery += 40
        # Log moving left
        else:
            self.rect.centerx -= Snake.MOVE_DIST
            # Frog has moved off screen
            if self.rect.right <= 0:
                diff = abs(snake.rect.left - self.rect.centerx)
                self.rect.centerx = Frog.SCREEN_DIM[0]/2
                self.rect.centery += 40