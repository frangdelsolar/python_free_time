def ask_players():
	try:
		return int(input('¿Cuántos jugadores? > '))
	except:
		print('Valor inválido')
		ask_players()


def ask_name(num_jugador):
	try:
		return str(input('¿Cuál es el nombre del {}º jugador? > '.format(num_jugador)))
	except:
		print('Valor inválido')
		ask_name()


def ask_arrojar_dados():
	try:
		user_input = str(input('Presioná "Enter" para arrojar los dados')) 
	except:
		print('Valor inválido')
		ask_arrojar_dados()
	if user_input == "":
		return True
	ask_arrojar_dados()
	
def ask_cambiar_dados():
	try:
		user_input = str(input('¿Querés cambiar dados (S/N)? >')).lower()
	except:
		print('Valor inválido')
		ask_cambiar_dados()
	if user_input == "s":
		return True
	elif user_input == 'n':
		return False
	ask_cambiar_dados()

def ask_cuantos_dados():
	try:
		user_input = int(input('¿Cuántos dados querés cambiar? > ')) 
	except:
		print('Valor inválido')
		ask_cuantos_dados()
	return user_input

def ask_cual_dado():
	try:
		user_input = int(input('¿Cuál dado querés cambiar? > ')) 
	except:
		print('Valor inválido')
		ask_cual_dado()
	return user_input

def ask_que_juego(player):
	try:
		user_input = (int(input('¿Cuál juego querés hacer? >')) -1)
	except:
		print('Valor inválido')
		ask_que_juego()
	return user_input