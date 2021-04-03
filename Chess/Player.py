class Player():
	def __init__(self, id, color):
		self.id = id
		self.name = ""
		self.pieces = []
		self.hand = []
		self.color = color
		self.build()

	def __str__(self):
		return self.name


	def build(self):
		self.name = input('Nombre del jugador: ')

		for i in self.pieces:
			i.color = self.color

	def show_pieces(self):
		for p in self.pieces:
			p.show()

	def show_hand(self):
		for p in self.hand:
			p.show()

