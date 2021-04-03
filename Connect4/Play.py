from Connect4 import *
from user import *
import pygame
import sys
import math

SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)
COLUMN_COUNT = 7
ROW_COUNT = 6
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

def draw_board(board, screen):
	for r in range(ROW_COUNT):
		for c in range(COLUMN_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			if board[r][c] == 0:
				pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

	for r in range(ROW_COUNT):
		for c in range(COLUMN_COUNT):

			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2:
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()
	

def play():
	
	juego = Connect4()
	game_over = False
	game_won = False
	turno = 0

	pygame.init()
	
	width = COLUMN_COUNT * SQUARESIZE
	height = (ROW_COUNT+1) * SQUARESIZE
	size = (width, height)
	screen = pygame.display.set_mode(size)
	
	juego.board.show()
	draw_board(juego.board.grid, screen)
	pygame.display.update()



	while (game_won==False) and (game_over==False):


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				

				


				print("Es el turno de ", juego.players[turno].color)
				# # col = ask_move()


				juego.move(turno, col)

				game_over = juego.check_over()
				game_won =  juego.check_won()

				if game_won:
					juego.board.show()
					draw_board(juego.board.grid, screen)

					print("Ganador: ", juego.players[turno].color)
					ask_again()

				if turno == 0:
					turno = 1
				else:
					turno = 0

				juego.board.show()
				draw_board(juego.board.grid, screen)


play()

