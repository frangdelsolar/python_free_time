from cards import Card, Deck, Player
from tabulate import tabulate
from user_input import ask_what_to_do, ask_row
from itertools import zip_longest



class CartaBlanca(object):
	def __init__(self):
		self.deck = []		
		self.org = [[],
					[],
					[],
					[],
					[],
					[],
					[],
					[],
					[],
					[],
					[],
					[],
					[]]
		self.player = 0
		self.deck_count = 0
		self.build()
		self.repartir()

	def build(self):
		self.deck = Deck()
		self.deck.shuffle()
		self.player = Player('jugador')


	def repartir(self):

		self.org[1].append(self.deck.drawCard())
		self.org[1][-1].shown = True

		for i in range(6, 13):
			self.org[i].append(self.deck.drawCard())

		for i in range(7, 13):
			self.org[i].append(self.deck.drawCard())
		
		for i in range(8, 13):
			self.org[i].append(self.deck.drawCard())

		for i in range(9, 13):
			self.org[i].append(self.deck.drawCard())

		for i in range(10, 13):
			self.org[i].append(self.deck.drawCard())

		for i in range(11, 13):
			self.org[i].append(self.deck.drawCard())

		for i in range(12, 13):
			self.org[i].append(self.deck.drawCard())

		for i in range(6,13):
			self.org[i][-1].shown = True


	def show_game(self, screen):
		def show_list(index):
			for c in self.org[index]:
				c.show()
				c.draw(screen)

		print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  ")
		print()
		# print("Estas son las cartas del mazo: ", self.deck.show())
		print("Mazo (0)                                                                               Nuevo Juego (99)")
		print("-{}-".format(self.deck_count))
		print()
		print()
		if len(self.org[1]) > 0:
			print('Pozo (1)', self.org[1][-1], end="                                  ")
		else: 
			print('Pozo (1)', end="                                                ")

		if len(self.org[2]) > 0:	
			print('(2)', self.org[2][-1], end="          ")
		else:
			print('Corazones (2)', end="          ")
		
		if len(self.org[3]) > 0:
			print("(3)", self.org[3][-1],end="          ")
		else:
			print("Diamantes (3)", end="          ")
		
		if len(self.org[4]) > 0:
			print('(4)', self.org[4][-1], end="          ")
		else:
			print("Tréboles (4)", end="          ")
		
		if len(self.org[5]) > 0:
			print('(5)', self.org[5][-1], end="          ")
		else:
			print("Picas (5)", end="          ")

		print()
		print()

		print("""    (6)                 (7)                 (8)                 (9)                 (10)                 (11)                 (12)""")
		
		card_list = [self.org[6],
					 self.org[7],
					 self.org[8],
					 self.org[9],
					 self.org[10],
					 self.org[11],
					 self.org[12]]

		for row in zip_longest(*card_list, fillvalue="            "):
			print ("         ".join(map(str, row)))


		print()
		print()
		self.player.show_hand()
		print()
		print()
		print("*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  ")
		print()
		print()

	
	def value_is_consecutive(self, card_to_take, opcion):
		if card_to_take.value == (self.org[opcion][-1].value - 1):
			return True
		return False

	def count_shown(self, opcion):
		r = 0
		for i in self.org[opcion]:
			if i.shown == True:
				r += 1
		return r

	def cut_list(self, col, index):
		col_len = len(self.org[col]) 
		for i in range(index, col_len):
			card = self.org[col].pop(-1)
			self.player.hand.append(card)

	def discard(self, col):
		c = self.player.hand.pop(-1)
		self.org[col].append(c)

	def discard_all(self, col):
		for i in self.player.hand:
			self.discard(col)

	def to_piles(self, card_to_take):

		# No funciona para valors mayores a 1

		if card_to_take.value == 1:
			return True
		
		else:

			print('Tu carta es mayor que 1')

			for i in range (2, 6):

				if i == 2:
					pile_suit = 'Cor'
				elif i == 3:
					pile_suit = 'Dia'
				elif i == 4:
					pile_suit = 'Tre'
				elif i == 5:
					pile_suit = 'Pic'


				print('Voy a comparar con la pila', i, "cuyo palo es ", pile_suit)


				if card_to_take.suit == pile_suit:

					print('Tu carta es de ese palo')

					if self.org[i] != []:

						print('El valor de tu carta ', card_to_take.value)
						print('El valor de la carta -1 de la pila', self.org[i][-1].value)
						print(card_to_take.value == (self.org[i][-1].value + 1))
						
						if (card_to_take.value == (self.org[i][-1].value + 1)):
							return True
			return False

	def color_is_opposite(self, card_to_take, opcion):

		if card_to_take.color != self.org[opcion][-1].color:
			return True
		return False


	def to_cols(self, card_to_take, opcion):

		# print('Estoy en to cols. Tu carta y tu opción', card_to_take, opcion)


		for i in range (6, 13):

			if i == opcion:			
				pass

			elif self.org[i] == []:
				if card_to_take.value == 13:

					print('Tu carta vale 13')

					return True
				pass
			else:

				# print('Debo verificar para las otras columnas', i)
				# print('Color opuesto', self.color_is_opposite(card_to_take,i))
				# print('Valor consecutivo', self.value_is_consecutive(card_to_take,i))

				if self.color_is_opposite(card_to_take, i):
					if self.value_is_consecutive(card_to_take, i):
						return True
		return False

	def take_card(self, card_to_take, opcion):

		# print("La carta que querés ", card_to_take)
		# print("La querés tomar de la pila ", opcion)
		# print('to piles: ', self.to_piles(card_to_take))
		# print('to cols: ', self.to_cols(card_to_take, opcion))
		
		if self.to_piles(card_to_take):
			self.org[opcion].pop(-1)
			self.player.hand.append(card_to_take)

		elif self.to_cols(card_to_take, opcion):
			self.org[opcion].pop(-1)
			self.player.hand.append(card_to_take)

	def comprobar_pilas(self):
		len_cor = len(self.org[2])
		len_dia = len(self.org[3])
		len_tre = len(self.org[4])
		len_pic = len(self.org[5])

		if len_cor == len_dia == len_tre == len_pic == 14:
			return True
		return False

	def check_others(self, card_to_take):
		min_val = 14

		for i in range(2, 6):
			if self.org[i]!= []:
				if self.org[i][-1].value < min_val:
					min_val = self.org[i][-1].value

		if card_to_take.value == 2:
			return True
		if card_to_take.value == min_val + 2:
			return True
		return False

	
	def send_to_piles(self, card_to_take):

		dos_mas_que_otros = self.check_others(card_to_take)

		for i in range (2, 6):

			if i == 2:
				pile_suit = 'Cor'
			elif i == 3:
				pile_suit = 'Dia'
			elif i == 4:
				pile_suit = 'Tre'
			elif i == 5:
				pile_suit = 'Pic'


			if card_to_take.suit == pile_suit:


				if card_to_take.value == 1:				
					self.org[i].append(card_to_take)
					return True

				elif self.org[i] != []:
					
					if (card_to_take.value == (self.org[i][-1].value + 1)):
						if dos_mas_que_otros:
							self.org[i].append(card_to_take)
							return True
		return False



	def resolver_obvias(self):
	
		if self.org[1] != []:
			if self.send_to_piles(self.org[1][-1]):
				self.org[1].pop(-1)
				if len(self.org[1]) > 0:
					self.org[1][-1].shown = True
	
		for i in range(6, 13):
			if self.org[i] != []:
				if self.send_to_piles(self.org[i][-1]):
					self.org[i].pop(-1)
					if len(self.org[i]) > 0:
						self.org[i][-1].shown = True
			else:
				continue
					

	def send_to_cols(self, card_to_take, opcion):

		for i in range (6, 13):

			if i == opcion:			
				pass

			elif self.org[i] == []:
				if card_to_take.value == 13:
					self.org[i].append(card_to_take)

					return True
				pass
			else:

				if self.color_is_opposite(card_to_take, i):
					if self.value_is_consecutive(card_to_take, i):
						self.org[i].append(card_to_take)
						return True
		return False


	def resolver_todo(self):
		if self.org[1] != []:
			if self.send_to_cols(self.org[1][-1], 1):
				self.org[1].pop(-1)
				if len(self.org[1]) > 0:
					self.org[1][-1].shown = True
	
		for i in range(6, 13):
			if self.org[i] != []:
				if self.send_to_cols(self.org[i][-1], i):
					self.org[i].pop(-1)
					if len(self.org[i]) > 0:
						self.org[i][-1].shown = True
			else:
				continue

		

	def accion(self, user_input):
		game_over = False
		game_won = False

		game_won = self.comprobar_pilas()

		op = user_input
		

		mano = self.player.hand

		self.resolver_obvias()
		# self.resolver_todo()


		empty_hand = False
		if mano == []:
			empty_hand = True

		if op == 99:
			game_over = True
		
		if op == 0:

			if len(self.deck) > 0:
				card_taken = self.deck.drawCard()
				self.org[1].append(card_taken)
				self.org[1][-1].shown = True
			
			elif self.deck_count < 3:
				# Reset deck
				for i in range((len(self.org[1])-1), 0, -1):
					card = self.org[1].pop(i)
					self.deck.cards.append(card)
					self.deck.cards[-1].shown = False			
				self.deck_count += 1
			
			else:
				print(self.deck_count)
				print('Game Over')
				game_over = True

		if op == 1:
			if empty_hand:
				try:
					card_to_take = self.org[1][-1]
					self.take_card(card_to_take, op)
				except:
					pass

		for i in range(2, 6):
			if op == 2:
				suit = 'Cor'
			if op == 3:
				suit = 'Dia'
			if op == 4:
				suit = 'Tre'
			if op == 5:
				suit = 'Pic'

			objetivo = self.org[i]

			if op == i:
				if empty_hand and objetivo != []:			
					card_to_take = objetivo[-1]
					self.take_card(card_to_take, op)

				if not empty_hand:
					card_to_discard = mano[-1]
					if card_to_discard.suit == suit:
						if len(objetivo) == 0:
							if card_to_discard.value == 1: 
								mano.pop(-1)					
								objetivo.append(card_to_discard)
						
						elif (card_to_discard.value == (objetivo[-1].value+1)):
							mano.pop(-1)
							objetivo.append(card_to_discard)
					else:
						print("No es posible!! Intenta otra cosa...")


		for i in range(6, 13):

			objetivo = self.org[i]

			if op == i:

				if empty_hand:
					reveladas = self.count_shown(op)
					print('Reveladas ', reveladas)
					print('Long de la pila ', len(objetivo))
					
					if reveladas == 1:
						ci = -1
						card_to_take = objetivo[ci]
						self.take_card(card_to_take, op)
						
						if len(objetivo) > 0:
							objetivo[-1].shown = True

					elif reveladas > 1:
						ci = ask_row()
						dif = len(objetivo) - reveladas
					
						if ci >= dif:
							
							print('To piles: ', self.to_piles(objetivo[ci]))
							print('To cols: ', self.to_cols(objetivo[ci], op))
							
							if self.to_piles(objetivo[ci]) or self.to_cols(objetivo[ci], op):
								self.cut_list(op, ci)
								if len(objetivo) > 0:
									objetivo[-1].shown = True
						else:
							pass

					
				elif not empty_hand:
					if objetivo == []:
						if mano[-1].value == 13:
							self.discard_all(op)
							try:
								self.discard(op)
							except:
								pass

					else:
						if self.color_is_opposite(mano[-1], op):
							if self.value_is_consecutive(mano[-1], op):
								self.discard_all(op)
								try:
									self.discard(op)
								except:
									pass
		return (game_over, game_won)



					













