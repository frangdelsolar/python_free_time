from Board import Board
from Player import Player

from Piece import *


class Chess():
	def __init__(self):
		self.board = Board()
		self.players = []
		self.build()

	def to_hand(self, row, col, player):
		pieza = self.board.grid[row][col]
		player.hand.append(pieza)
		self.board.grid[row][col] = "  "


	def is_own(self, row_base, col_base, player):
		origen = self.board.grid[row_base][col_base]
		if not origen in player.pieces:
			print("Esa pieza no es tuya!!!")
			return False
		return True

	def move_is_valid(self, row_base, col_base, row_dest, col_dest, player):

		def none_diags(row_base, col_base, row_dest, col_dest):
			r = row_dest - row_base
			c = col_dest - col_base

			dif = abs(r)

			print(r, c)

			if r > 0 and c > 0:
				for i in range(dif, 1, -1):
					if self.board.grid[row_base + i][col_base + i]:
						return False
				return True

			elif r < 0 and c < 0:
				for i in range(dif, 1, -1):
					if self.board.grid[row_base - i][col_base - i]:
						return False
				return True

			elif r > 0 and c < 0:
				for i in range(dif, 1, -1):
					if self.board.grid[row_base + i][col_base - i]:
						return False
				return True

			elif r < 0 and c > 0:
				for i in range(dif, 1, -1):
					if self.board.grid[row_base - i][col_base + i]:
						return False
				return True


		origen = self.board.grid[row_base][col_base]
		destino = self.board.grid[row_dest][col_dest]
		
		# Peón
		if origen.type == "Peón":
			if player.color == "b":
				if row_dest == row_base-1:
					
					if col_base == col_dest:
						if not destino:
							return True

					elif (col_base == (col_dest - 1)):
						if destino.color != origen.color:
							return True

					elif (col_base == (col_dest + 1)):
						if destino.color != origen.color:
							return True

				elif row_base == 6:
					if row_dest == row_base-2:
						if (row_base + 1):
							if col_base == col_dest:
								if not destino:
									return True

			if player.color == "n":
				if row_dest == row_base+1:
					
					if col_base == col_dest:
						if not destino:
							return True

					elif (col_base == (col_dest - 1)):
						if destino.color != origen.color:
							return True

					elif (col_base == (col_dest + 1)):
						if destino.color != origen.color:
							return True

				elif row_base == 1:
					if row_dest == row_base+2:
						if col_base == col_dest:
							if not destino:
								return True
			

		# Caballo
		elif origen.type == "Caballo":
			if ((row_dest == (row_base+2)) or (row_dest == (row_base-2))) and ((col_dest == (col_base+1)) or (col_dest == (col_base-1))):
				if not destino:
					return True	
				elif destino.color != origen.color:
					return True		
			elif ((row_dest == (row_base+1)) or (row_dest == (row_base-1))) and ((col_dest == (col_base+2)) or (col_dest == (col_base-2))):
				if not destino:
					return True	
				elif destino.color != origen.color:
					return True				

		# Alfil
		elif origen.type == "Bishop":
			if abs(row_dest - row_base) == abs(col_dest - col_base):
				if none_diags(row_base, col_base, row_dest, col_dest):
					if not destino:
						return True
					elif destino.color != origen.color:
						return True

		# Torre
		elif origen.type == "Torre":
			if ((row_dest != row_base) and (col_dest == col_base)) \
				or ((row_dest == row_base) and (col_dest != col_base)):
				if not destino:
					return True
				elif destino.color != origen.color:
					return True


		# Reina
		elif origen.type == "Queen":
			if ((row_dest != row_base) and (col_dest == col_base)) \
				or ((row_dest == row_base) and (col_dest != col_base)) \
				or abs(row_dest - row_base) == abs(col_dest - col_base):
				if not destino:
					return True
				elif destino.color != origen.color:
					return True

		# Rey
		elif origen.type == "King":
			if (((row_dest != row_base) and (col_dest == col_base)) \
							or ((row_dest == row_base) and (col_dest != col_base)) \
							or abs(row_dest - row_base) == abs(col_dest - col_base)) \
							and (abs(row_dest - row_base) == 1 \
								or abs(col_dest - col_base) == 1):
				# if is_out_of_scope():
				if not destino:
					return True
				elif destino.color != origen.color:
					return True


		print("Movimiento inválido")
		return False

	def move_piece(self, row, col, player):
		self.board.grid[row][col] = player.hand[-1]
		player.hand.pop(-1)


	def build(self):
		# Asignar un color a los jugadores
		for i in range(2):
			if i == 0:
				color = "b"
			else:
				color = "n"
			self.players.append(Player(i, color))

		# Peones blancos y negros
		for i in range(8):
			peon = Peon()
			self.players[0].pieces.append(peon)
			self.board.grid[6][i] = peon

		for i in range(8):
			peon = Peon()
			self.players[1].pieces.append(peon)
			self.board.grid[1][i] = peon

		# Caballos
		kb1 = Knight()
		kb2 = Knight()
		self.players[0].pieces.append(kb1)
		self.players[0].pieces.append(kb2)
		self.board.grid[7][1] = kb1
		self.board.grid[7][6] = kb2

		kn1 = Knight()
		kn2 = Knight()
		self.players[1].pieces.append(kn1)
		self.players[1].pieces.append(kn2)
		self.board.grid[0][1] = kn1
		self.board.grid[0][6] = kn2


		# Alfiles
		bb1 = Bishop()
		bb2 = Bishop()
		self.players[0].pieces.append(bb1)
		self.players[0].pieces.append(bb2)
		self.board.grid[7][2] = bb1
		self.board.grid[7][5] = bb2

		bn1 = Bishop()
		bn2 = Bishop()
		self.players[1].pieces.append(bn1)
		self.players[1].pieces.append(bn2)
		self.board.grid[0][2] = bn1
		self.board.grid[0][5] = bn2

		# Torres
		tb1 = Torre()
		tb2 = Torre()
		self.players[0].pieces.append(tb1)
		self.players[0].pieces.append(tb2)
		self.board.grid[7][0] = tb1
		self.board.grid[7][7] = tb2

		tn1 = Torre()
		tn2 = Torre()
		self.players[1].pieces.append(tn1)
		self.players[1].pieces.append(tn2)
		self.board.grid[0][0] = tn1
		self.board.grid[0][7] = tn2

		# Reyes
		rb = King()
		self.players[0].pieces.append(rb)
		self.board.grid[7][4] = rb

		rn = King()
		self.players[1].pieces.append(rn)
		self.board.grid[0][4] = rn



		# Reinas
		qb = Queen()
		self.players[0].pieces.append(qb)
		self.board.grid[7][3] = qb

		qn = Queen()
		self.players[1].pieces.append(qn)
		self.board.grid[0][3] = qn

		# Asignar color a las piezas
		for i in range(2):
			for j in range(len(self.players[i].pieces)):
				self.players[i].pieces[j].color = self.players[i].color


	def show(self):
		self.board.show()
