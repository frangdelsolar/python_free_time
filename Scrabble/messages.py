def ask_players():
	try:
		players = int(input("Cuántos jugadores? "))
		return players
	except:
		print("Error! Volvé a intentar ")
		ask_players()

def ask_player_name():
	try:
		name = str(input("Nombre: "))
		return name
	except:
		print("Error! Volvé a intentar ")
		ask_player_name()