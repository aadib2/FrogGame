import pygame,sys, random
#from "file name" import "class name"
from frog import Frog
from cactus import Cactus
from bee import Bee
from street import Street
from rivers import River



pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])


SCREEN_DIM = WIDTH,HEIGHT = 600,500
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption('Frog Road Game!')
CLOCK = pygame.time.Clock()
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (81, 175, 116)
YELLOW = (100, 85, 0)
BROWN = (182, 150, 95)
GRAY = (175, 175, 175)
BLUE = (46,143,229)
ORANGE = (226,166, 93)
TAN = (234,206,172)
LIGHT_BLUE = (159,211,250)

FONT = pygame.font.Font('resources/joystix monospace.ttf', 20)
MENU_BIG = pygame.font.Font('resources/joystix monospace.ttf', 60)
MENU_MED = pygame.font.Font('resources/joystix monospace.ttf', 25)
MENU_SMALL = pygame.font.Font('resources/joystix monospace.ttf', 15)

MENU_IMAGE = pygame.image.load('resources/desert.png')
FROG_IMAGE = pygame.image.load('resources/Frog.png')
START_MENU = True
END_MENU = False
END_MENU_IMG = pygame.image.load('resources/desertskullremoved.png')
END_MENU_BG = pygame.image.load('resources/desertbackgremoved.png')
SUN_IMG = pygame.image.load('resources/SUN.png')

frog = Frog()
bee = Bee(Bee.STARTING_POSITION, 'Right')
# create street objects
streets = []
number_of_cacti = 3
street_height = 400

#create river objects
rivers = []
number_of_snakes = 3
river_height = 150
for _ in range(2):
    rivers.append(River(river_height, 'Left', random.randint(1, number_of_snakes)))
    rivers.append(River(river_height - 30, 'Right', random.randint(1, number_of_snakes)))
    river_height -= 60

# for loop used to set up 2 sets of streets in opposite directions
for _ in range(2):
      streets.append(Street(street_height, 'Left', random.randint(1, number_of_cacti)))
      streets.append(Street(street_height - 60, 'Right', random.randint(1, number_of_cacti)))
      street_height -= 120

#variables to keep track of score
score = 0
high_score = 0
current_best = 0


#game loop
while(True):
    CLOCK.tick(FPS)
    SCREEN.fill(TAN)

    for event in pygame.event.get():
    # this allows the user to close the window.
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # W
                frog.move_up()
            if event.key == pygame.K_a:  # A
                frog.move_left()
            if event.key == pygame.K_s:  # S
                frog.move_down()
            if event.key == pygame.K_d:  # D
                frog.move_right()

    #while loop for when menu screen is displayed
    while START_MENU:
        CLOCK.tick(15)
        SCREEN.fill(BLUE)
        #variables for text objects
        name = MENU_BIG.render('FROG ROAD:', True, WHITE)
        subtitle = MENU_MED.render('DESERT EDITION', True, WHITE)
        instructions = MENU_SMALL.render('Press Space to Start', True, WHITE)
        #display text on menu screen
        SCREEN.blit(name, (75,130))
        SCREEN.blit(subtitle, (150, 200))
        SCREEN.blit(instructions, (180, 250))
        SCREEN.blit(MENU_IMAGE, (0,260))
        SCREEN.blit(FROG_IMAGE, (250, 325))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    START_MENU = False

        pygame.display.update()

    # while loop to display end menu
    while END_MENU:
        CLOCK.tick(15)
        SCREEN.fill(LIGHT_BLUE)
        #text variables for end menu
        thx = MENU_MED.render('Thanks for Playing!', True, WHITE)
        scores = MENU_MED.render('Your Final Score: %d' % (score + current_best), True, WHITE)
        instructions = MENU_SMALL.render('Press \'Space\' To Play Again', True, WHITE )
        #draw text onto the screen
        SCREEN.blit(thx, (85, 100))
        SCREEN.blit(scores, (70, 160))
        SCREEN.blit(instructions, (130, 220))
        SCREEN.blit(END_MENU_BG, (0, 200))
        SCREEN.blit(SUN_IMG, (500, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    END_MENU = False
                    #reset variables if restarting game
                    score = 0
                    current_best = 0
                    frog.lives = 3


        pygame.display.update()

    # Act on rivers and snakes
    frog_on_snake = False  # new
    for river in rivers:
        # Draw River
        SCREEN.fill(BLUE, river.rect)

        # Log
        for snake in river.snakes:
            SCREEN.blit(snake.image, snake.rect)
            snake.move()
            if frog.rect.colliderect(snake.rect):
                frog.move_on_snake(snake)
                frog_on_snake = True  # new

        # Collided with River and not a Log - new
        if not frog_on_snake and frog.rect.colliderect(river.rect):
            frog.reset_position()

    if frog.rect.colliderect(bee.rect):
        frog.reset_position()

    bee.move()

    # loop through each street and draw cacti, also resets frog if collides with cactus
    for street in streets:
        SCREEN.fill(GRAY, street.rect)
        for cactus in street.cacti:
            SCREEN.blit(cactus.image, cactus.rect)
            cactus.move()
            if frog.rect.colliderect(cactus.rect):
                frog.reset_position()
    # draw cactus and frog sprite onto the screen
    SCREEN.blit(bee.image, bee.rect)
    SCREEN.blit(frog.image, frog.rect)


    if 475 - frog.rect.top > current_best:
        current_best = 475-frog.rect.top
    if score + current_best >= high_score:
        high_score = score+current_best
    if frog.rect.top <= 60:
        frog.reset_position()
        frog.lives+=1
        score+=1000 + current_best
        current_best = 0

    # text object variables
    score_text = FONT.render("Score: " + str(score + current_best), True, WHITE)
    high_score_text = FONT.render("High Score: " + str(high_score), True, WHITE)
    lives_text = FONT.render("Lives: " + str(frog.lives), True, WHITE)

    # draw the text onto the screen
    SCREEN.blit(score_text, (5,0))
    SCREEN.blit(high_score_text, (5,20))
    SCREEN.blit(lives_text, (5,40))

    #if statement that checks if the lives have run out,then end screen will be displayed
    if frog.lives == 0:
        END_MENU = True


    pygame.display.flip()

pygame.quit()