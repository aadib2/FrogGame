import pygame,random
from snake import Snake

class River:
    SIZE = (600,30)
    SCREEN_DIM = 600,500

    def __init__(self, river_height, direction, number_of_snakes):
        self.rect = pygame.Rect((0, river_height), River.SIZE)
        self.snakes = []

        self.add_snakes(direction,number_of_snakes, river_height + 15)

    def add_snakes(self, direction: str, number_of_snakes: int, river_height: int):
        dp = []
        for _ in range(number_of_snakes):
            while True:
                x_pos = random.randint(30, 570)
                valid = True
                for i in range(x_pos - 60, x_pos + 60):
                    if i in dp:
                        valid = False
                if valid:
                    dp.append(x_pos)
                    break
            self.snakes.append(Snake((x_pos, river_height), direction))
