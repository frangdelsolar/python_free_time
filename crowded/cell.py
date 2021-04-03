from config import *
from vector import *
import pygame
import random

class Cell(object):
	
	def __init__(self):
		self.row = 0
		self.col = 0
		self.vecindad = []
		self.habitantes = []

	def update(self):
		for i in self.habitantes:
			ind = self.habitantes.index(i)
			if self.row != i.row or self.col != i.col:
				self.habitantes.pop(ind)

		for i in self.habitantes:
			if i.equipo != 0:
				for j in self.habitantes:
					if j.equipo == 0:
						if Vector(i.coord(), j.coord()).distance() <= i.size*3:
							j.equipo = i.equipo
							j.color = (200, 0, 200)
							i.seguidores.append(j)
				
		
	def draw(self, screen):
		pygame.draw.rect(screen, (50, 50, 50), (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE), 1)	
