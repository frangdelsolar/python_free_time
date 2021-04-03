from Scrabble import Scrabble
from config import *
from Fichas import Ficha
import pygame
import sys
import math


def play():

	game_over = False
	game_won = False
	
	pygame.init()

	s = Scrabble()
	turno = s.players[0]

	while game_over == False and game_won == False:

		screen = pygame.display.set_mode(screen_size)

		s.draw(screen, turno)
		pygame.display.update()

		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				sys.exit()		

			if event.type == pygame.MOUSEBUTTONDOWN:
				
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				posy = event.pos[1]
				row = int(math.floor(posy/SQUARESIZE))

				print(row, col)

				if row == 15 and (col <= 10 and col >= 13):
					print("hola")
					# Botón de terminar la jugada


				if not turno.seleccion:

					if row == 16:
						turno.hand[col].seleccionada = True
						turno.seleccion = turno.hand[col]
						ind = turno.hand.index(turno.seleccion)
						turno.hand.pop(ind)


					if event.type == pygame.MOUSEBUTTONDOWN:
						posx2 = event.pos[0]
						col2 = int(math.floor(posx2/SQUARESIZE))

						posy2 = event.pos[1]
						row2 = int(math.floor(posy2/SQUARESIZE))

				else:
					turno.seleccion.row = row
					turno.seleccion.col = col
					turno.seleccion.seleccionada = False
					s.board.fichas.append(turno.seleccion)		
					pygame.display.update()	
					turno.seleccion = None

			if turno.seleccion:
				mouse_position = pygame.mouse.get_pos()
				turno.seleccion.x = mouse_position[0]
				turno.seleccion.y = mouse_position[1]
				turno.seleccion.draw(screen)
				pygame.display.update()


	for i in range(len(s.players)):
		s.players[i].show()
		
play()