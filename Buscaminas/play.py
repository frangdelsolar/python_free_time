from config import *
from user import *
from buscaminas import *
from board import *
import pygame
import sys
import math


def play():
	
	# size = ask_size()
	# bombs = ask_bombs()


	board = Board(size, bombs)
	game_over = False
	game_won = False

	pygame.init()
	pygame.display.set_caption('Buscaminas')
	a = pygame.image.load('img/mine.png')
	pygame.display.set_icon(a)
	
	clock = pygame.time.Clock()
	while game_over == False and game_won == False:

		screen = pygame.display.set_mode(screen_size)
	
		board.draw(screen)
		pygame.display.update()

		board.show_board()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				posy = event.pos[1]
				row = int(math.floor(posy/SQUARESIZE))
			
				# w = ask_what()
				w = "r"
				c = col	
				r = row

				# if w == "b":
				if event.button == RIGHT:
					if board.grid[r][c].placeholder == "P":
						board.grid[r][c].placeholder = "."
					else:
						board.grid[r][c].placeholder = "P"
			
				else:
					if board.grid[r][c].value == "@":
						board.reveal()
						# board.grid[r][c].revelar_vecinos(screen)
						board.revelar(screen, clock, board.grid[r][c])
						board.draw(screen)
						pygame.display.update()
						print("Game Over")
						game_over = True
					else:
						reveal_cell(board, r, c, clock, screen)
						game_won = check_win(board)
						



	# play_again = ask_again()
	# if play_again == "s":
	# 	play()
	# else:
	# 	print("Gracias por jugar!!!")
	
play()
