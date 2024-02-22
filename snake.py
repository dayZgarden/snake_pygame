import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((640, 600))
pygame.display.set_caption('Snake')

# CONSTANTS

SNAKE_SPEED = .5
TILE_SIZE = 32
BOARD_WIDTH = 17 * TILE_SIZE
BOARD_HEIGHT = 15 * TILE_SIZE
GRID =  BOARD_WIDTH * BOARD_HEIGHT

def snake(snake_x, snake_y, snake_width, snake_height):
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(snake_x, snake_y, snake_width, snake_height))

def switchHeightAndWidth(width, height):

    temp = width
    width = height
    height = temp

    return (width, height)

def keyPressed():

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        return 'd'
    if keys[pygame.K_a]:
        return 'a'
    if keys[pygame.K_w]:
        return 'w'
    if keys[pygame.K_s]:
        return 's'

def move_snake(last_key, snake_x, snake_y, snake_width, snake_height):

    UPPER_BOUND, LEFT_BOUND = 0,0
    RIGHT_BOUND = 640 - snake_width
    LOWER_BOUND = 600 - snake_height

    while last_key == 'd':
        if snake_x < RIGHT_BOUND:
            snake_x += SNAKE_SPEED
        break
    while last_key == 'a':
        if snake_x > LEFT_BOUND:
            snake_x -= SNAKE_SPEED
        break
    while last_key == 'w':
        if snake_y > UPPER_BOUND:
            snake_y -= SNAKE_SPEED
        break
    while last_key == 's':
        if snake_y < LOWER_BOUND:
            snake_y += SNAKE_SPEED
        break

    return (snake_x, snake_y, snake_width, snake_height)

def fruit():
    pygame.draw.circle(screen, (255, 255, 255), (random.randint(0, 640), random.randint(0, 600)), TILE_SIZE / 2)

def scoreboard(player_score):

    font = pygame.font.Font(None, 48)
    score_text = font.render(str(player_score), 1, (255,255,255))
    screen.blit(score_text, (10, 10))

def highscore(highscore):

    font = pygame.font.Font(None, 48)
    score_text = font.render(str(highscore), 1, (255,255,255))
    screen.blit(score_text, (600, 10))

def collision():
    pass

def add_tail():
    pass

def drawGrid():
    for i in range(0, BOARD_WIDTH, TILE_SIZE):
        pygame.draw.line(screen, (255,255,255), (i, 0), (i, 600))
    for i in range(0, BOARD_HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, (255,255,255), (0, i), (640, i))


def main(): 

    global snake_x, snake_y, snake_width, snake_height, player_score, last_key
    snake_width = 3 * TILE_SIZE
    snake_height = TILE_SIZE
    snake_x = 100
    snake_y = 200
    player_score = 0
    last_key = 'd'

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0))
        last_key = keyPressed()
        snake_x, snake_y, snake_width, snake_height = move_snake(last_key, snake_x, snake_y, snake_width, snake_height)
        snake(snake_x, snake_y, snake_width, snake_height)
        drawGrid()
        fruit()
        scoreboard(player_score)
        highscore(10)

        pygame.display.flip()

    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()