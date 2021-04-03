from config import *
from level import Level
import pygame
import sys

def main():
	game_over = False

	pygame.init()

	l = Level()

	while not game_over:

		screen = pygame.display.set_mode(SCREEN_SIZE)
		screen.fill((50,50,50))

		mousex, mousey = pygame.mouse.get_pos()

		l.update()
		l.draw(screen)


		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

main()