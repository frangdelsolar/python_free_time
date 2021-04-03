def ask_size():
	try:
		user_input = int(input('¿Qué tamaño quieres que tenga el tablero? > '))
		return user_input
	except:
		print('Valor inválido')
		ask_size()

def ask_again():
	try:
		user_input = str(input('¿Quieres jugar de nuevo? (S/N) > ')).lower()
	except:
		print('Valor inválido')
		ask_again()
	return user_input