from solitario import CartaBlanca
from cards import *
from user_input import ask_col, ask_row, ask_jugar_again
import pygame
import sys

c_width = 36 
c_height = 30 
SQUARE_SIZE = 25

width = SQUARE_SIZE * c_width
height = SQUARE_SIZE * c_height
screen_size = (width, height)
TURQUESA = (135, 206, 235)

def play():

	game_over = False
	game_won = False
	
	sol = CartaBlanca()

	pygame.init()

	screen = pygame.display.set_mode(screen_size)
	screen.fill(TURQUESA)

	c = Card(2, 'Dia', 'R', 'img/corazon.png')
	c.show()
	c.shown = True

	
	while not game_over or game_won:


		c.draw(screen)


		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		sol.show_game(screen)
		# col = ask_col()
		# game_over, game_won = sol.accion(col)

		if game_over:
			again = ask_jugar_again()
			if again == 1:
				play()
			else:
				print("Muchas gracias!!!")

		if game_won:
			again = ask_jugar_again()
			if again == 1:
				play()
			else:
				print("Muchas gracias!!!")


		

play()