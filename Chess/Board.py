class Board():
	def __init__(self):
		self.grid = [[0, 0, 0, 0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 0, 0]
					 ]
		self.build()

	def build(self):
		for i in range(8):
			for j in range(8):
				self.grid[i][j] = None
				

	def show(self):

		print("       0    1    2    3    4    5    6    7   ")
		print("    ----------------------------------------- ")
		for i in range(8):
			print(" ", i, end=" ")
			for j in range(8):
				if self.grid[i][j] == None:
					print("|   ", end=" ")
				else:
					print("|",self.grid[i][j], end=" ")
			print("|")
			print("    ----------------------------------------- ")


