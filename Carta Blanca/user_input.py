def ask_row():
	try:
		user_input = int(input('Fila> ')) 
	except:
		print('Valor inválido')
		ask_row()
	if user_input > -1:
		return user_input

		
def ask_col():
	try:
		user_input = int(input('Columna> '))
		if user_input > -1:
				return user_input 
	except:
		print('Valor inválido')
		ask_col()


def ask_what_to_do():
	try:
		user_input = int(input('Tomar(1) o dejar(2)? > ')) 
	except:
		print('Valor inválido')
		ask_what_to_do()
	return user_input

def ask_jugar_again():
	try:
		user_input = int(input('Volver a jugar, Sí(1) o No(2)? > ')) 
	except:
		print('Valor inválido')
		ask_jugar_again()
	return user_input