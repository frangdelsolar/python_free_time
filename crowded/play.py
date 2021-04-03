from vector import *
from punto import *
from config import *
from level import Level
import pygame
import sys



def play():
	game_over = False

	pygame.init()

	contador = 0

	level = Level()
	
	mouseclick = (0,0)

	while not game_over:

		screen = pygame.display.set_mode(SCREEN_SIZE)
		level.update()
		level.draw(screen)
		level.puntos[0].detenerse(mouseclick)

		print(len(level.puntos[0].seguidores))

		pygame.display.update()

		contador += 1
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:

				posx = event.pos[0]
				posy = event.pos[1]
				mouseclick = (posx, posy)

				vm = Vector(level.puntos[0].coord(), mouseclick)
				xspeed, yspeed = vm.unit()
				level.puntos[0].xspeed = xspeed
				level.puntos[0].yspeed = yspeed	

play()