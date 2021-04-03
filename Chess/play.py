from chess import Chess
from input import *
import pygame
import sys
import math

SQUARESIZE = 100

GREY = (220, 220, 220)
DARK_GREY = (169, 169, 169)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


def draw_board(board, screen, size):
	# myfont.set_bold(True)

	for r in range(size):
		for c in range(size):
			

			# Dibujar tablero
			if r % 2 == 0:
				if c % 2 == 0:
					pygame.draw.rect(screen, GREY, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE))
				else:
					pygame.draw.rect(screen, BLACK, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE))
			
			elif r % 2 == 1:
				if c % 2 == 0:
					pygame.draw.rect(screen, BLACK, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE))
				else:
					pygame.draw.rect(screen, GREY, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE))
	
			pygame.draw.rect(screen, DARK_GREY, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE), 5)
			

			# Dibujar piezas
			


def play_chess():

	chess = Chess()
	game_over = False
	game_won = False
	player = chess.players[0]

	pygame.init()
	size = 8
	width = size * SQUARESIZE
	height = (size) * SQUARESIZE
	screen_size = (width, height)
	screen = pygame.display.set_mode(screen_size)

	draw_board(chess.board, screen, size)
	pygame.display.update()


	while game_over == False and game_won == False:

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()


				if event.type == pygame.MOUSEBUTTONDOWN:

					chess.show()

					print("Es el turno de ", player, player.color)

					print("Qué pieza querés mover?")
					row_base = ask_row()
					col_base = ask_col()

					is_own = chess.is_own(row_base, col_base, player)
					
					while is_own == True:

						print("A dónde querés ubicarla?")
						row_dest = ask_row()
						col_dest = ask_col()

						# Chequear si el movimiento es válido
						is_valid = chess.move_is_valid(row_base, col_base, row_dest, col_dest, player)

						if is_valid:
							chess.to_hand(row_base, col_base, player)
							chess.move_piece(row_dest, col_dest, player)
							is_own = False

						else:
							pass


						# if is_valid:
						# 	if player == chess.players[0]:
						# 		player = chess.players[1]
						# 	else:
						# 		player = chess.players[0]

					else:
						pass



play_chess()