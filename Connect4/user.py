def ask_move():
	try:
		move = int(input('Dónde va tu ficha? '))
		if move >= 0 and move < 7:
			return move
		else:
			print("0 - 7")
			ask_move()
	except:
		print("Error!! Volvé a intentar")
		ask_move()

def ask_again():
	try:
		again = str(input('Jugar de nuevo? ')).lower()
		if again == "s" or again == "n":
			return again
		else:
			print("S - N")
			ask_move()
	except:
		print("Error!! Volvé a intentar")
		ask_move()