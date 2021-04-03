import random
import pygame
from vector import *
from config import *

class Punto(object):

	def __init__(self):
		self.x= random.randint(0, WIDTH) 
		self.y = random.randint(0, HEIGHT)
		self.xspeed = 0
		self.yspeed = 0
		self.color = (255, 255, 255)
		self.size = 10
		self.row = int(self.y//SQUARESIZE)
		self.col = int(self.x//SQUARESIZE)
		self.seguidores = []
		self.lastx = 0
		self.lasty = 0
		self.equipo = 0


	def coord(self):
		return (self.x, self.y)

	def detenerse(self, coord):
		x, y = coord
		if (int(self.x) >= int(x)-1 and int(self.x) <= int(x)+1) and (int(self.y) >= int(y)-1 and int(self.y) <= int(y)+1):
			self.xspeed=0
			self.yspeed=0

	def update(self, board):
		if self.x != self.lastx:
			self.lastx = self.x
		if self.y != self.lasty:
			self.lasty = self.y

		self.x += self.xspeed
		self.y += self.yspeed	
		
		self.row = int(self.y//SQUARESIZE)
		self.col = int(self.x//SQUARESIZE)


		for p in self.seguidores:
			print(p.seguidores)
			vector = Vector(p.coord(), self.coord())			
			if vector.distance() >= self.size*2:
				xspeed, yspeed = vector.unit()
				p.xspeed = xspeed
				p.yspeed = yspeed
			else:
				p.x = p.lastx
				p.y = p.lasty

	
	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))
		pygame.draw.rect(screen, (255, 0, 0), (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE), 1)	



