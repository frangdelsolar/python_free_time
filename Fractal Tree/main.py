from vector import *
from config import *
import pygame
import sys

from tree import Tree



def play():
	game_over = False

	pygame.init()

	tree = Tree()

	contador = 0	

	while not game_over:

		screen = pygame.display.set_mode(SCREEN_SIZE)
		screen.fill((7, 26, 76, 100))
		pygame.display.update()

		# if contador % 100 == 0:
		tree.update()
		tree.draw(screen)
		

		contador += 1

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pass


play()