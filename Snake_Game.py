import random
import pygame
import os

#This is the command to initialse the pygame
pygame.init()

#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
blush = (255,240,245)

# Setting Hight and Width
screen_width = 750
screen_hight = 450

font = pygame.font.SysFont(None,50)

#creating clock variable
clock = pygame.time.Clock()

#creating Window
gameWindow = pygame.display.set_mode((screen_width, screen_hight))

#setting Title
pygame.display.set_caption("Snake Game")
pygame.display.update()



#for snake length
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


#function to print score on screen
def text_on_screen(text,color,x,y):
    screen_text = font.render(text ,True, color)

#update screen
    gameWindow.blit(screen_text,[x,y])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((0,255,255))
        text_on_screen("Welcome to Snakes", black, 195, 145)
        text_on_screen("Press Space Bar To Play", black, 160, 190)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)

# Creating a game loop
def gameloop():

    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 100
    snake_y = 100
    score = 0

# Check if hiscore file exists
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("High_score.txt", "r") as f:
        High_score = f.read()

    snake_list = []
    snake_length = 1

    # for continous moment
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5

    snake_size = 20
    food_size = 20
    fps = 50  # frames per second

    # snake food
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_hight / 2)

    while not exit_game:
        if game_over:

            with open("High_score.txt", "w") as f:
                f.write(str(High_score))

            gameWindow.fill(white)
            text_on_screen("Game Over! Press Enter To Continue", red, 65, 165)

#if clicked on cross symbol quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

#if enter key is pressed continue the game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():

# handling quit event
                if event.type == pygame.QUIT:
                    exit_game = True

# Handling key event
                if event.type == pygame.KEYDOWN:

# for right arrow key
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

# for left arrow key
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

# for up arrow key
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

# for down arrow key
                    if event.key == pygame.K_DOWN:
                        velocity_y = + init_velocity
                        velocity_x = 0

#cheat code
                    if event.key == pygame.K_m:
                        score += 10

#for snakes continous moment
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) <10 and abs(snake_y - food_y) <10:
                score = score + 10

#displaying food on screen
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_hight / 2)

#for snake length
                snake_length = snake_length + 5

#for high score
                if score > int(High_score):
                    High_score = score

# filling white color for background
            gameWindow.fill(blush)

#displaying score on screen
            text_on_screen("Score: " + str(score)  + "                                   High score: "+ str(High_score), blue, 10, 10)

# Creating snake food
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])

# Creating snake head
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

# Deleting the snake head
            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_hight:
                game_over = True

            plot_snake(gameWindow, black,snake_list, snake_size,)

        pygame.display.update()

# frames per second
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
