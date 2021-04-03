import pygame
from rama import Rama
from config import *
import random

class Tree():
	def __init__(self):
		self.ramas = []
		self.build()

	def build(self):
		self.ramas.append(Rama(int(width//2), height, int(width//2), height-200))

	def update(self):
		for rama in self.ramas:
			if rama.sarmientos == False:
				r1 = Rama(rama.x2, rama.y2, random.randint(0, width), random.randint(0, height))
				r2 = Rama(rama.x2, rama.y2, random.randint(0, width), random.randint(0, height))
				self.ramas.append(r1)
				self.ramas.append(r2)
				rama.sarmientos = True
				break
			else:
				pass


	def draw(self, screen):
		for rama in self.ramas:
			rama.draw(screen)
			pygame.display.update()


