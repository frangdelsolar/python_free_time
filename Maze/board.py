from config import *
from cell import *
import random
import copy
import pygame


class Board(object):

	def __init__(self, size):
		self.size = size
		self.grid = [[0] * self.size for r in range(self.size)]
		self.build()

	def build(self):

		for i in range(self.size):
			for j in range(self.size):
				self.grid[i][j] = Cell()
				self.grid[i][j].row = i
				self.grid[i][j].col = j
				self.grid[i][j].visited = False


		for i in range(self.size):
			for j in range(self.size):
				# Casillas del centro
				if i>0 and (i<(self.size-1)) and j>0 and (j<(self.size-1)): 
					self.grid[i][j].vecindad = [                    (self.grid[i-1][j]),                   
												(self.grid[i][j-1]), 						(self.grid[i][j+1]),
												                    (self.grid[i+1][j])                   ]
				
				# Esquina superior izquierda
				elif i==0 and j == 0:
					self.grid[i][j].vecindad = [(self.grid[i][j+1]), (self.grid[i+1][j])]

				# Esquina inferior izquierda
				elif i==(self.size-1) and j == 0:
					self.grid[i][j].vecindad = [(self.grid[i-1][j]), (self.grid[i][j+1]),]
		
				# Esquina sup derecha
				elif i==0 and j == (self.size-1):
					self.grid[i][j].vecindad = [(self.grid[i][j-1]), (self.grid[i+1][j]),]

				# Esquina inf derecha
				elif i==(self.size-1) and j == (self.size-1):
					self.grid[i][j].vecindad = [(self.grid[i-1][j]), (self.grid[i][j-1]),]

				
				# Casillas contra el techo (no esquinas)
				elif i==0 and j>0 and (j<(self.size-1)):
					self.grid[i][j].vecindad = [(self.grid[i][j-1]), (self.grid[i][j+1]), 
												(self.grid[i+1][j])]
				
				# Casillas contra el suelo(no esquinas)
				elif i==(self.size-1) and j>0 and (j<(self.size-1)):
					self.grid[i][j].vecindad = [ (self.grid[i-1][j]), (self.grid[i][j-1]), (self.grid[i][j+1]),]


				# Casillas junto a la pared izq (no esquinas)
				elif i>0 and (i<(self.size-1)) and j == 0:
					self.grid[i][j].vecindad = [(self.grid[i-1][j]),  (self.grid[i][j+1]),
												(self.grid[i+1][j])]

				# Casillas contra pared derecha(no esquinas)
				elif i>0 and (i<(self.size-1)) and j == (self.size-1):
					self.grid[i][j].vecindad = [(self.grid[i-1][j]), (self.grid[i][j-1]),
												 (self.grid[i+1][j]),]

	def show(self):
		print("----------------------------")
		for r in range(size):
			for c in range(size):
				print(self.grid[r][c], end="  ")
			print()
		print("----------------------------")
		print()

	def draw(self, screen, current):
		self.show()

		for r in range(size):
			for c in range(size):
				self.grid[r][c].draw(screen, current)
