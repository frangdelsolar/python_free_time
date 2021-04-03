from level import Level
from config import *
import pygame
import sys


def play():
	
	pygame.init()
	pygame.display.set_caption('Pacman')

	clock = pygame.time.Clock()

	level = Level()

	game_over = False
	game_won = False
	
	while game_over == False and game_won==False:

		screen = pygame.display.set_mode(screen_size)
		level.draw(screen)
		pygame.display.update()

		game_won = level.check_win()
		game_over = level.check_over()

		if game_over:
			print("Over")
		if game_won:
			print("Won")

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_DOWN:
					direccion = (0, 1)
					# if level.pacman.can_move(level.board, direccion):
					level.pacman.dir(direccion)
				if event.key == pygame.K_UP:
					direccion = (0, -1)
					# if level.pacman.can_move(level.board, direccion):
					level.pacman.dir(direccion)
				if event.key == pygame.K_LEFT:
					direccion = (-1, 0)
					# if level.pacman.can_move(level.board, direccion):
					level.pacman.dir(direccion)
				if event.key == pygame.K_RIGHT:
					direccion = (1, 0)
					# if level.pacman.can_move(level.board, direccion):
					level.pacman.dir(direccion)
play()