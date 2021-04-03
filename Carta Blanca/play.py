from cartablanca import CartaBlanca
from cards import Player
from user_input import ask_col, ask_row, ask_jugar_again

def play():

	game_over = False
	game_won = False
	
	sol = CartaBlanca()
	
	while not game_over or game_won:

		sol.show_game()
		col = ask_col()
		game_over, game_won = sol.accion(col)

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