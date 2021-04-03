
class Board():
	def __init__(self):
		self.grid = [[0, 0, 0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 0],
					 [0, 0, 0, 0, 0, 0, 0]]

	def show(self):
		print(" 0  1  2  3  4  5  6")
		print(" -------------------")
		for i in self.grid:
			print(i)
		print(" -------------------")
