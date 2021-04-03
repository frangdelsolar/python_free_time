import pygame
import random

from snake import Snake

SIZE = 10
HEIGHT = SIZE * 60
WIDTH = SIZE * 60
SCREEN_SIZE = (WIDTH, HEIGHT)

def main():

    run = True
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    snake = Snake(30, 30)

    # while run:
    #     pass


main()
