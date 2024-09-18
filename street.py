import pygame, random
from cactus import Cactus

class Street:
    # Define constants for dimensions and street size
    SIZE = (600, 40)
    SCREEN_DIM = 600, 500

    def __init__(self, street_height: int, direction:str, number_of_cacti:int):
        self.rect = pygame.Rect((0, street_height), Street.SIZE)
        self.cacti = []
        # adds cacti onto the screen randomly without overlap
        self.add_cacti(direction, number_of_cacti, street_height+20)

    def add_cacti(self, direction: str, number_of_cacti: int, street_height: int):
        dp = []
        for _ in range(number_of_cacti):
            while True:
                x_pos = random.randint(30, 570)
                valid = True
                for i in range(x_pos - 60, x_pos + 60):
                    if i in dp:
                        valid = False
                if valid:
                    dp.append(x_pos)
                    break
            self.cacti.append(Cactus((x_pos, street_height), direction))