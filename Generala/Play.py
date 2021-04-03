from player import (Dado,
					Player, 
					Juego, 
					)
from user_input import (ask_players, 
						ask_arrojar_dados, 
						ask_cambiar_dados,
						ask_que_juego,
						)


def play():
	num_players = ask_players()
	juego = Juego(num_players)
	juego.show()

	while juego.game_over == False:
		turno = 0
		jugador = juego.players[turno]
		print('Es el turno de: ', jugador.nombre)
		arrojar = ask_arrojar_dados()
		if arrojar:
			jugador.randomize()
			jugador.show_mano()


			si_cambia = ask_cambiar_dados()
			if si_cambia:
				jugador.cambiar_dados()

				si_cambia2 = ask_cambiar_dados()
				if si_cambia2:
					jugador.cambiar_dados()


			# Qué juego elige?
			opcion = ask_que_juego(jugador)
			jugador.sumar_puntos(opcion)
			jugador.show_juegos()
					




play()

# f = Player('f')
# f.mano[0].value = 1
# f.mano[1].value = 1
# f.mano[2].value = 1
# f.mano[3].value = 1
# f.mano[4].value = 1

# f.show_mano()

# f.sumar_puntos(10)
# f.show_juegos()

