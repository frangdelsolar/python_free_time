from config import *
import pygame
import random

class Cell(object):
	
	def __init__(self):
		self.row = 0
		self.col = 0
		self.x = 0
		self.y = 0
		self.walls = [True, True, True, True]
		self.visited = False
		self.vecindad = []
		self.marcada = False

	def __str__(self):
		if self.visited:
			return '0'
		return '.'
		

	def check_vecinos(self):
		vecinos = []
		
		for v in self.vecindad:
			if not v.visited:
				vecinos.append(v)
		
		if len(vecinos)>0:
			return random.choice(vecinos)
		
		return None


	def choose_next(self):
		cell = random.choice(self.vecindad)
		return cell

	def draw(self, screen, current, cars):

		if self.visited:
			pygame.draw.rect(screen, (100, 50, 100), (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))	
		else:
			pygame.draw.rect(screen, (50, 50, 50), (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))	

		x = self.col * SQUARESIZE
		y = self.row * SQUARESIZE

		if self.walls[0]:
			pygame.draw.line(screen,(100, 100, 100), (x,            y),            (x+SQUARESIZE, y))
		if self.walls[1]:
			pygame.draw.line(screen,(100, 100, 100), (x+SQUARESIZE, y),            (x+SQUARESIZE, y+SQUARESIZE))

			
		if self.walls[2]:
			pygame.draw.line(screen,(100, 100, 100), (x+SQUARESIZE, y+SQUARESIZE), (x           , y+SQUARESIZE))
		if self.walls[3]:
			pygame.draw.line(screen,(100, 100, 100), (x,            y+SQUARESIZE), (x,            y))
		

		pygame.draw.rect(screen, (0, 255, 0), (current.col * SQUARESIZE, current.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))	


	def draw_grey(self, screen, cars):

		pygame.draw.rect(screen, (50, 50, 50), (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))	

		x = self.col * SQUARESIZE
		y = self.row * SQUARESIZE

		if self.walls[0]:
			pygame.draw.line(screen,(100, 100, 100), (x,            y),            (x+SQUARESIZE, y))
						
		if self.walls[1]:
			pygame.draw.line(screen,(100, 100, 100), (x+SQUARESIZE, y),            (x+SQUARESIZE, y+SQUARESIZE))

			
		if self.walls[2]:
			pygame.draw.line(screen,(100, 100, 100), (x+SQUARESIZE, y+SQUARESIZE), (x           , y+SQUARESIZE))
		if self.walls[3]:
			pygame.draw.line(screen,(100, 100, 100), (x,            y+SQUARESIZE), (x,            y))
		

