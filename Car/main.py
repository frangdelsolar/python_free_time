import pygame
import sys
import random

from config import *
from car import Car
from vector import Vector
from level import Level



def play():
	
	pygame.init()
	pygame.display.set_caption('Bricks Breaker')

	clock = pygame.time.Clock()

	game_over = False
	game_won = False

	level = Level()

	while game_over == False and game_won==False:

		screen = pygame.display.set_mode(screen_size)
		level.update()
		level.draw(screen)

		pygame.display.update()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:

				posx = event.pos[0]
				posy = event.pos[1]
				mouseclick = (posx, posy)					
					
				vm = Vector(level.cars[0].coord(), mouseclick)
				xspeed, yspeed = vm.unit()
				level.cars[0].xspeed = xspeed
				level.cars[0].yspeed = yspeed

				level.cars[0].xacc = xspeed*0.01
				level.cars[0].yacc = yspeed*0.01

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE:
					level.cars[0].teletransport(level.board)
					level.cars[1].teletransport(level.board)

				if event.key == pygame.K_DOWN:
					if level.cars[0].state == 0:					
						direccion = (0, 1)
					else:
						direccion = (0, -1)
					level.cars[0].dir(direccion)
				
				if event.key == pygame.K_UP:
					if level.cars[0].state == 0:
						direccion = (0, -1)
					else:
						direccion = (0, 1)						
					level.cars[0].dir(direccion)

				if event.key == pygame.K_LEFT:
					if level.cars[0].state == 0:
						direccion = (-1, 0)
					else:
						direccion = (1, 1)
					level.cars[0].dir(direccion)

				if event.key == pygame.K_RIGHT:
					if level.cars[0].state == 0:
						direccion = (1, 0)
					else:
						direccion = (-1, 0)
					level.cars[0].dir(direccion)

				if event.key == pygame.K_s:
					if level.cars[1].state == 0:
						direccion = (0, 1)
					else:
						direccion = (0, -1)
					level.cars[1].dir(direccion)

				if event.key == pygame.K_w:
					if level.cars[1].state == 0:
						direccion = (0, -1)
					else:
						direccion = (0, 1)
					level.cars[1].dir(direccion)

				if event.key == pygame.K_a:
					if level.cars[1].state == 0:
						direccion = (-1, 0)
					else:
						direccion = (1, 0)
					level.cars[1].dir(direccion)

				if event.key == pygame.K_d:
					if level.cars[1].state == 0:
						direccion = (1, 0)
					else:
						direccion = (-1, 0)
					level.cars[1].dir(direccion)


			
play()