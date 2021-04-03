from input import *
from treesandtents import *
from board import *
import pygame
import sys
import math


SQUARESIZE = 30

BLACK = (0, 0, 0)
DARK_GREY = (169, 169, 169)
GREY = (220,220,220)
GREEN = (0, 255, 0)


BLUE = (3, 35, 67)
RED = (195, 2, 2)
BROWN = (173, 122, 91)
YELLOW = (221, 185, 130)


LEFT = 1
RIGHT = 3


def play():

	def draw_board(board, screen, size):
		
		myfont = pygame.font.SysFont("Arial", 15)
		myfont.set_bold(True)

		for r in range(size):
			for c in range(size):

				pygame.draw.rect(screen, GREY, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE), 3)
			
				if board.grid[r][c].placeholder == '.':
					pygame.draw.rect(screen, BLACK, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))

					if board.grid[r][c].value == 1:
						pygame.draw.rect(screen, GREEN, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE))


				elif board.grid[r][c].placeholder == 'pasto':
					pygame.draw.rect(screen, GREY, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))

				elif board.grid[r][c].placeholder == 'tienda':
					pygame.draw.rect(screen, RED, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))




				# if board.grid[r][c].value == 2:
				# 	pygame.draw.rect(screen, RED, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE))

			
				if c == size - 1:
					label = myfont.render(str(board.row_tents[r]), 1, BLACK)
					pygame.draw.rect(screen, DARK_GREY, (c*SQUARESIZE+SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))
					screen.blit(label, (int(c*SQUARESIZE+SQUARESIZE+SQUARESIZE/4), int(r*SQUARESIZE+ SQUARESIZE/4)))
			
				if r == size-1:
					label = myfont.render(str(board.col_tents[c]), 1, BLACK)
					pygame.draw.rect(screen, DARK_GREY, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
					screen.blit(label, (int(c*SQUARESIZE+SQUARESIZE/4), int(r*SQUARESIZE+ SQUARESIZE + SQUARESIZE/4)))




	size = ask_size()
	board = Board(size)
	board.show()

	pygame.init()
	width = (size+1) * SQUARESIZE
	height = (size+1) * SQUARESIZE
	screen_size = (width, height)
	screen = pygame.display.set_mode(screen_size)
	draw_board(board, screen, size)
	pygame.display.update()


	game_over = False
	game_won = False

	while game_over == False and game_won == False:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


			if event.type == pygame.MOUSEBUTTONDOWN:
				
				posx = event.pos[0]
				c = int(math.floor(posx/SQUARESIZE))

				posy = event.pos[1]
				r = int(math.floor(posy/SQUARESIZE))

				if event.button == LEFT:

					if board.grid[r][c].placeholder == ".":
						board.grid[r][c].placeholder = "pasto"
						board.grid[r][c].resuelta = True


					elif board.grid[r][c].placeholder == "pasto":
						board.grid[r][c].placeholder = "tienda"
						board.grid[r][c].resuelta = True
					
					elif board.grid[r][c].placeholder == "tienda":
						board.grid[r][c].placeholder = "."
						board.grid[r][c].resuelta = False

					draw_board(board, screen, size)
					pygame.display.update()
			

				game_won = check_win(board)

	draw_board(board, screen, size)
	pygame.display.update()

	play_again = ask_again()
	if play_again == "s":
		play()
	else:
		print("Gracias por jugar!!!")
	
play()
