import random
import copy


class Cell(object):
	
	def __init__(self):
		self.row = 0
		self.col = 0
		self.value = None
		self.posibilidad = [0, 1, 2]
		self.cruz = []
		self.vecindad = []
		self.resuelta = False
		self.placeholder = "."


	def show(self):
		print("({}, {}). Mi valor es {}.".format(self.row, self.col, self.value))

class Board(object):

	def __init__(self, size):
		self.size = size
		self.arboles = (size*size*23//100)
		self.grid = [[0] * self.size for r in range(self.size)]
		self.row_tents = []
		self.col_tents = []

		self.build()
		self.acampar()
		self.plantar_arboles()
		self.contar_carpas()

	def build(self):

		for i in range(self.size):
			for j in range(self.size):
				valor = copy.deepcopy(self.grid[i][j])
				self.grid[i][j] = Cell()
				self.grid[i][j].row = i
				self.grid[i][j].col = j
				self.grid[i][j].value = None
				self.grid[i][j].resuelta = False
				
		# vecinos en cruz
		for i in range(self.size):
			for j in range(self.size):
				# Casillas del centro
				if i>0 and (i<(self.size-1)) and j>0 and (j<(self.size-1)): 
					self.grid[i][j].cruz = [(self.grid[i-1][j]), (self.grid[i][j-1]),
											(self.grid[i][j+1]), (self.grid[i+1][j])]
				
				# Esquina superior izquierda
				elif i==0 and j == 0:
					self.grid[i][j].cruz = [(self.grid[i][j+1]), (self.grid[i+1][j])]

				# Esquina inferior izquierda
				elif i==(self.size-1) and j == 0:
					self.grid[i][j].cruz = [(self.grid[i-1][j]), (self.grid[i][j+1]),]
		
				# Esquina sup derecha
				elif i==0 and j == (self.size-1):
					self.grid[i][j].cruz = [(self.grid[i][j-1]), (self.grid[i+1][j]),]

				# Esquina inf derecha
				elif i==(self.size-1) and j == (self.size-1):
					self.grid[i][j].cruz = [(self.grid[i-1][j]), (self.grid[i][j-1]),]

				
				# Casillas contra el techo (no esquinas)
				elif i==0 and j>0 and (j<(self.size-1)):
					self.grid[i][j].cruz = [(self.grid[i][j-1]), (self.grid[i][j+1]),  
												(self.grid[i+1][j]),]
				
				# Casillas contra el suelo(no esquinas)
				elif i==(self.size-1) and j>0 and (j<(self.size-1)):
					self.grid[i][j].cruz = [ (self.grid[i-1][j]), 
												(self.grid[i][j-1]), (self.grid[i][j+1]),]


				# Casillas junto a la pared izq (no esquinas)
				elif i>0 and (i<(self.size-1)) and j == 0:
					self.grid[i][j].cruz = [(self.grid[i-1][j]), (self.grid[i][j+1]),
												(self.grid[i+1][j]), ]

				# Casillas contra pared derecha(no esquinas)
				elif i>0 and (i<(self.size-1)) and j == (self.size-1):
					self.grid[i][j].cruz = [ (self.grid[i-1][j]), (self.grid[i][j-1]),
												 (self.grid[i+1][j]),]

		# todos los vecinos
		for i in range(self.size):
			for j in range(self.size):
				# Casillas del centro
				if i>0 and (i<(self.size-1)) and j>0 and (j<(self.size-1)): 
					self.grid[i][j].vecindad = [(self.grid[i-1][j-1]),(self.grid[i-1][j]),(self.grid[i-1][j+1]),
												(self.grid[i][j-1]), 						(self.grid[i][j+1]),
												(self.grid[i+1][j-1]),(self.grid[i+1][j]),(self.grid[i+1][j+1])]
				
				# Esquina superior izquierda
				elif i==0 and j == 0:
					self.grid[i][j].vecindad = [(self.grid[i][j+1]), (self.grid[i+1][j]), (self.grid[i+1][j+1])]

				# Esquina inferior izquierda
				elif i==(self.size-1) and j == 0:
					self.grid[i][j].vecindad = [(self.grid[i-1][j]), (self.grid[i-1][j+1]), (self.grid[i][j+1]),]
		
				# Esquina sup derecha
				elif i==0 and j == (self.size-1):
					self.grid[i][j].vecindad = [(self.grid[i][j-1]), (self.grid[i+1][j-1]), (self.grid[i+1][j]),]

				# Esquina inf derecha
				elif i==(self.size-1) and j == (self.size-1):
					self.grid[i][j].vecindad = [(self.grid[i-1][j-1]), (self.grid[i-1][j]), (self.grid[i][j-1]),]

				
				# Casillas contra el techo (no esquinas)
				elif i==0 and j>0 and (j<(self.size-1)):
					self.grid[i][j].vecindad = [(self.grid[i][j-1]), (self.grid[i][j+1]), (self.grid[i+1][j-1]), 
												(self.grid[i+1][j]), (self.grid[i+1][j+1])]
				
				# Casillas contra el suelo(no esquinas)
				elif i==(self.size-1) and j>0 and (j<(self.size-1)):
					self.grid[i][j].vecindad = [(self.grid[i-1][j-1]), (self.grid[i-1][j]), (self.grid[i-1][j+1]),
												(self.grid[i][j-1]), (self.grid[i][j+1]),]


				# Casillas junto a la pared izq (no esquinas)
				elif i>0 and (i<(self.size-1)) and j == 0:
					self.grid[i][j].vecindad = [(self.grid[i-1][j]), (self.grid[i-1][j+1]), (self.grid[i][j+1]),
												(self.grid[i+1][j]), (self.grid[i+1][j+1])]

				# Casillas contra pared derecha(no esquinas)
				elif i>0 and (i<(self.size-1)) and j == (self.size-1):
					self.grid[i][j].vecindad = [(self.grid[i-1][j-1]), (self.grid[i-1][j]), (self.grid[i][j-1]),
												(self.grid[i+1][j-1]), (self.grid[i+1][j]),]


	def acampar(self):
		print('Estoy acampando', self.arboles)
		
		for b in range(self.arboles):
			
			i = random.randint(0, self.size-1)
			j = random.randint(0, self.size-1)

			
			# Si ningún vecino es carpa 
			if self.grid[i][j].value == None:
				
				vecinos = []
				for v in self.grid[i][j].vecindad:
					if v.value == 2:
						vecinos.append(v)

				if len(vecinos) == 0:
					self.grid[i][j].value = 2
					self.grid[i][j].resuelta = False

	
	def plantar_arboles(self):

		def ubicar_carpa(celda):
			c = random.choice(celda.cruz)
			if c.value == None:
				c.value = 1
				c.resuelta = True
			else:
				print("No puedo ser árbol", i, j)

				index = celda.cruz.index(c)

				celda.cruz.pop(index)
				ubicar_carpa(celda)


		for i in range(self.size):
			for j in range(self.size):
				if self.grid[i][j].value == 2:

					ubicar_carpa(self.grid[i][j])		
	
	def contar_carpas(self):

		for i in self.grid:
			tent_count = 0
			
			for j in i:
				if j.value == 2:
					tent_count += 1

			self.row_tents.append(tent_count) 

		

		for i in range (self.size):
			tent_count = 0
			for j in range (self.size):
				if self.grid[j][i].value == 2:
					tent_count += 1

			self.col_tents.append(tent_count)





	def show(self):
		separador = '  * ' * self.size
		print(separador)
		print()
		for i in range(self.size):
			if i==0:
				print("    ", end="")
				for j in range(self.size):
					if j < 10:
						print(j, end="  ")
					else:
						print(j, end=" ")
				print()


			for j in range(self.size):

				if j == 0:
					if i<10:
						print(i, end= "   ")
					else:
						print(i, end= "  ")

				# if self.grid[i][j].is_revealed:
				print(self.grid[i][j].value, end="  ")
				# else:
				# 	print(self.grid[i][j].placeholder, end="  ")
			print("")
		print()
		print(separador)



def check_win(board):
	print("Grid lenght", board.size**2)
	resueltas = []
	for i in range (board.size):
		for j in range(board.size):
			if board.grid[i][j].value == 2 and not board.grid[i][j].resuelta:
				print("Te estás mandando cualquiera")
				return False
	
	if len(resueltas) == (board.size**2):
		return True



