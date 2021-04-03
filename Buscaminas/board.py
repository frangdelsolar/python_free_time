from config import *
from cell import *
import random
import copy
import pygame


class Board(object):

	def __init__(self, size, bombs):
		self.size = size
		self.bombs = bombs
		self.grid = [[0] * self.size for r in range(self.size)]
		self.build()
		self.bombas()
		self.calc_values()


	def build(self):

		for i in range(self.size):
			for j in range(self.size):
				valor = copy.deepcopy(self.grid[i][j])
				self.grid[i][j] = Cell()
				self.grid[i][j].row = i
				self.grid[i][j].col = j
				self.grid[i][j].value = 0
				self.grid[i][j].is_revealed = False


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


	def bombas(self):
		for b in range(self.bombs):
			
			i = random.randint(0, self.size-1)
			j = random.randint(0, self.size-1)
			self.grid[i][j].value = "@"


	def calc_values(self):
		for i in range(self.size):
			for j in range(self.size):
				count_bombs = 0

				if self.grid[i][j].value != "@":
					for item in self.grid[i][j].vecindad:
						if item.value == "@":
							count_bombs +=1

					if count_bombs == 0:
						self.grid[i][j].value = 0
					self.grid[i][j].value = count_bombs

	def reveal(self):
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

				if self.grid[i][j].value == "@":
					print(self.grid[i][j].value, end="  ")

				elif self.grid[i][j].value != "@":
					if self.grid[i][j].value < 10:
						print(self.grid[i][j].value, end="  ")
				else:
					print(self.grid[i][j].value, end="   ")
			print("")
		print()
		print(separador)

		for i in range(self.size):
			for j in range(self.size):
				self.grid[i][j].is_revealed = True

	def revelar(self, screen, clock, cell):

		for r in range(size):
			for c in range(size):

				self.grid[r][c].draw(screen)
				pygame.display.update()
				clock.tick(200)

		

	def draw(self, screen):
		for r in range(size):
			for c in range(size):
				self.grid[r][c].draw(screen)


	def show_board(self):
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

				if self.grid[i][j].is_revealed:
					print(self.grid[i][j].value, end="  ")
				else:
					print(self.grid[i][j].placeholder, end="  ")
			print("")
		print()
		print(separador)