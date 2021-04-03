from user_input import (ask_name, 
						ask_cuantos_dados, 
						ask_cual_dado)
import random

class Dado(object):
	def __init__(self):
		self.value = 0
		self.index = 0

	def show(self):
		print("{}º) Valor: {}".format(self.index, self.value))


class Jugada(object):
	def __init__(self):
		self.id = 0
		self.nombre = ""
		self.puntaje = 0
		self.tachada = False

	def show(self):
		print("{}). {}. {}.".format(self.id, self.nombre, self.puntaje), end=" ")
		if self.tachada == True:
			print("NO disponible", end=" ")
		print()


class Player(object):
	def __init__(self, nombre):
		self.nombre = nombre
		self.juegos=[]
		self.mano=[]
		self.build()

	def build(self):
		for i in range(5):
			dado = Dado()
			dado.index = i
			self.mano.append(dado)

		for i in range(1, 12):
			jugada = Jugada()
			jugada.id = i
			jugada.puntaje = 0
			jugada.tachada = False

			if i == 11:
				jugada.nombre = 'Doble generala'

			elif i == 10:
				jugada.nombre = 'Generala'

			elif i == 9:
				jugada.nombre = 'Poker'

			elif i == 8:
				jugada.nombre = 'Full'
			
			elif i == 7:
				jugada.nombre = 'Escalera'

			elif i == 6:
				jugada.nombre = 'Sumar 6'

			elif i == 5:
				jugada.nombre = 'Sumar 5'

			elif i == 4:
				jugada.nombre = 'Sumar 4'

			elif i == 3:
				jugada.nombre = 'Sumar 3'

			elif i == 2:
				jugada.nombre = 'Sumar 2'

			elif i == 1:
				jugada.nombre = 'Sumar 1'

			self.juegos.append(jugada)


	def randomize(self):
		for dado in self.mano:
			dado.value = random.randint(1,6)

	def show_mano(self):
		print('Dados de ', self.nombre)
		for i in range(1,7):
			for dado in self.mano:
				if dado.value==i:
					dado.show()
			
	def show_juegos(self):
		for j in self.juegos:
			j.show()
		self.show_puntaje()

	def show_puntaje(self):
		print ('Puntaje total: ', self.calc_puntuacion())

	def calc_puntuacion(self):
		puntos = 0
		for i in self.juegos:
			puntos += i.puntaje
		return puntos

	def cambiar_dados(self):
		cant_dados = ask_cuantos_dados()
		for i in range(cant_dados):
			i_dado = ask_cual_dado()
			self.mano[i_dado].value = random.randint(1,6)
		self.show_mano()


	def sumar_puntos(self, opcion):

		def suma_num(num):
			puntos = 0
			for i in self.mano:
				if i.value == num:
					puntos += num
			return puntos

		def hay_full(values):
			set_val = set(values)
			if len(set_val) == 2:
				a, b = set_val
				a_count = values.count(a)
				b_count = values.count(b)
				if (a_count == 2 and b_count == 3) or (a_count == 3 and b_count == 2):
					return True
			return False

		def hay_escalera(valores):

			if valores[1] == valores[0] + 1:			
				if valores[2] == valores[1] + 1:			
					if valores[3] == valores[2] + 1:						
						if valores[4] == valores[3] + 1: 
							return True
			return False


		def hay_poker(values):
			v = values
			for i in range(1,7):
				if v.count(i) >= 4:
					return i
			return 0
			

		def hay_generala(values):
			for i in range(1,7):
				if values.count(i) == 5:
					return i
			return 0
			

		def hay_doble_generala(values):
			for i in range(1,7):
				if values.count(i) == 5 and self.juegos[10].puntaje > 0:
					return i
			return 0


		def get_values():
			values = []
			for i in self.mano:
				v = i.value
				values.append(v)
			values = sorted(values)
			return values


		opcion = opcion
		p = 0
		values = get_values()

		# Revisar puntaje doble generala!!!
		if opcion == 10:
			dg = hay_doble_generala(values)
			p = 100
		
		elif opcion == 9:
			g = hay_generala(values)
			p = 60

		
		elif opcion == 8:
			po =  hay_poker(values)
			p = values.count(po) * po

		
		elif opcion == 7:
			if hay_full(values):
				for i in values:
					p += i
					

		elif opcion == 6:
			if hay_escalera(values):
				for i in values:
					p += i
	
		elif opcion == 5:
			p = suma_num(6)

		elif opcion == 4:
			p = suma_num(5)
		
		elif opcion == 3:
			p = suma_num(4) 

		elif opcion == 2:
			p = suma_num(3) 

		elif opcion == 1:
			p = suma_num(2) 					
		
		elif opcion == 0:
			p = suma_num(1)

		self.juegos[opcion].puntaje = p
		self.juegos[opcion].tachada = True 
		self.calc_puntuacion()


class Juego(object):
	def __init__(self, jugadores):
		self.players = []
		self.game_over = False
		self.build(jugadores)

	def build(self, jugadores):
		for i in range(jugadores):
			nombre = ask_name(i)
			jugador = Player(nombre)

			self.players.append(jugador)

	def show(self):
		for i in self.players:
			i.show_juegos()



