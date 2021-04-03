import random

size = 1


class Board():
	def __init__(self):
		self.grid =[[0] * size  for i in range(size)]
		self.build()

	def build(self):
		nums = []
		
		for i in range(size*size):
			nums.append(i)

		for i in range(size):
			for j in range(size):

				randChoice = random.choice(nums)
				self.grid[i][j] = randChoice

				index = nums.index(randChoice)
				nums.pop(index)


			 	

	def show(self):
		for i in self.grid:
			print(i)

