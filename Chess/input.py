def ask_row():
	try:
		u_input = int(input("Fila: "))
		if u_input < 0 or u_input > 7:
			ask_row()
		return u_input
	except:
		print("Error! Intentá de nuevo")
		ask_row()

	

def ask_col():
	try:
		u_input = int(input("Columna: "))
		if u_input < 0 or u_input > 7:
			ask_col()
		return u_input
	except:
		print("Error! Intentá de nuevo")
		ask_col()

	
