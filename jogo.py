import pygame
from pygame.locals import *
import random

TELA = (600, 600)
PIXEL = 10


def collision(pos1, pos2):
    return pos1 == pos2


def offlimits(pos):
    if 0 <= pos[0] < TELA[0] and 0 <= pos[1] < TELA[1]:
        return False
    else:
        return True


def random_on_grid():
    x = random.randint(0, TELA[0])
    y = random.randint(0, TELA[1])
    return x // PIXEL * PIXEL, y // PIXEL * PIXEL


pygame.init()
screen = pygame.display.set_mode(TELA)
pygame.display.set_caption('Snake')

snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEL, PIXEL))
snake_surface.fill((255, 255, 0))
snake_direction = K_LEFT

apple_surface = pygame.Surface((PIXEL, PIXEL))
apple_surface.fill((255, 0, 0))
apple_pos = random_on_grid()


def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_pos = random_on_grid()


while True:
    pygame.time.Clock().tick(15)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    screen.blit(apple_surface, apple_pos)

    if collision(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        apple_pos = random_on_grid()

    for pos in snake_pos:
        screen.blit(snake_surface, pos)

    screen.blit(apple_surface, apple_pos)

    for i in range(len(snake_pos)-1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]):
            restart_game()
        snake_pos[i] = snake_pos[i-1]

    if offlimits(snake_pos[0]):
        restart_game()

    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - PIXEL, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEL, snake_pos[0][1])

    pygame.display.update()
