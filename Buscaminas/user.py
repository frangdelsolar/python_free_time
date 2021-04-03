def ask_row():
	try:
		user_input = int(input('Fila> ')) 
	except:
		print('Valor inválido')
		ask_row()
	return user_input 
		
def ask_col():
	try:
		user_input = int(input('Columna> ')) 
	except:
		print('Valor inválido')
		ask_col()
	return user_input

def ask_size():
	try:
		user_input = int(input('¿Qué tamaño quieres que tenga el tablero? > ')) 
	except:
		print('Valor inválido')
		ask_size()
	return user_input

def ask_bombs():
	try:
		user_input = int(input('¿Cuántas bombas deseas? > ')) 
	except:
		print('Valor inválido')
		ask_bombs()
	return user_input

def ask_again():
	try:
		user_input = str(input('¿Quieres jugar de nuevo? (S/N) > ')).lower()
	except:
		print('Valor inválido')
		ask_again()
	return user_input

def ask_what():
	try:
		user_input = str(input('¿Bandera o Revelar? (B/R) > ')).lower()
	except:
		print('Valor inválido')
		ask_what()
	if user_input == "b" or user_input == "r":
		return user_input
	ask_what()