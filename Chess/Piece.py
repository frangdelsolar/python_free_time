class Piece():
	def __init__(self, tipo, placeholder, captured):
		self.type = tipo
		self.placeholder = placeholder
		self.captured = captured
		self.color = ""
		self.row = None
		self.col = None
		self.img = 'bird.png'

	def __str__(self):
		return "{}{}".format(self.placeholder, self.color)

	def show(self):
		print("{}{}. ({},{})".format(self.placeholder, self.color, self.row, self.col))
		
		pieceImg = pygame.image.load(self.img)
		pieceImg = pygame.transform.scale(pieceImg, (60, 60))
		screen.blit(pieceImg, (0, 0))

class Peon(Piece):
	def __init__(self):
		Piece.__init__(self, 'Peón', "P", False)


class Knight(Piece):
	def __init__(self):
		Piece.__init__(self, 'Caballo', "C", False)

class Bishop(Piece):
	def __init__(self):
		Piece.__init__(self, 'Bishop', "B", False)

class Torre(Piece):
	def __init__(self):
		Piece.__init__(self, 'Torre', "T", False)

class King(Piece):
	def __init__(self):
		Piece.__init__(self, 'King', "K", False)

class Queen(Piece):
	def __init__(self):
		Piece.__init__(self, 'Queen', "Q", False)

