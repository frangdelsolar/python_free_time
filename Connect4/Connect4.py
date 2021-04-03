from Tablero import *
from Players import *


class Connect4():

	def __init__(self):
		self.board = 0
		self.players = []
		self.build()

	def build(self):
		self.board = Board()

		p1 = Player(1)
		p2 = Player(2)
		self.players.append(p1)
		self.players.append(p2)

	def move(self, turno, col):
		
		for i in range(5, -1, -1):
			if self.board.grid[i][col] == 0:
				self.board.grid[i][col] = self.players[turno].color
				break

	def check_over(self):
		for i in range(6):
			for j in range(7):
				if self.board.grid[i][j] == 0:
					return False
		return True

	def check_won(self):
		def rows4():
			for i in range(6):
				for j in range(4):
					if self.board.grid[i][j] == self.board.grid[i][j+1] == self.board.grid[i][j+2] == self.board.grid[i][j+3]:
						if self.board.grid[i][j] != 0:
							return True
							break
			return False			

		def cols4():
			for i in range(3):
				for j in range(7):
					if self.board.grid[i][j] == self.board.grid[i+1][j] == self.board.grid[i+2][j] == self.board.grid[i+3][j]:
						if self.board.grid[i][j] != 0:
							return True
							break

			

		def diags4():
			for i in range(3):
				for j in range(4):
					if self.board.grid[i][j] == self.board.grid[i+1][j+1] == self.board.grid[i+2][j+2] == self.board.grid[i+3][j+3]:
						if self.board.grid[i][j] != 0:
							return True
							break

			for i in range(3):
				for j in range(3, 7):
					if self.board.grid[i][j] == self.board.grid[i+1][j-1] == self.board.grid[i+2][j-2] == self.board.grid[i+3][j-3]:
						if self.board.grid[i][j] != 0:
							return True
							break


		if rows4() or cols4() or diags4():
			print("Tenemos un ganador")
			self.board.show()
			return True
		return False
