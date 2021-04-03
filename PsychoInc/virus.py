from sistemas import SISTEMAS
from config import *
import random
import pygame
import math


class Virus():
	def __init__(self, sistema):
		self.x = random.randint(SQUARESIZE*5, WIDTH - SQUARESIZE)
		self.y = random.randint(SQUARESIZE, (HEIGHT - (SQUARESIZE*2)))
		self.col = int(math.floor(self.x/SQUARESIZE))
		self.row = int(math.floor(self.y/SQUARESIZE))
		self.time = random.randint(0, 2500)
		self.sistema = sistema
		self.agresividad = random.random() * 0.1
		self.size = 1//self.agresividad
		self.image = ''
		self.constrain()
		self.set_image()


	def set_image(self):
		if self.sistema == 0:
			self.image = pygame.image.load('img/v0.png')
		if self.sistema == 1:
			self.image = pygame.image.load('img/v1.png')
		if self.sistema == 2:
			self.image = pygame.image.load('img/v2.png')
		if self.sistema == 3:
			self.image = pygame.image.load('img/v3.png')
		if self.sistema == 4:
			self.image = pygame.image.load('img/v4.png')
		if self.sistema == 5:
			self.image = pygame.image.load('img/v5.png')
		if self.sistema == 6:
			self.image = pygame.image.load('img/v6.png')
		if self.sistema == 7:
			self.image = pygame.image.load('img/v7.png')


		self.image = pygame.transform.scale(self.image, (int(self.size), int(self.size)))

	def constrain(self):

		if self.size > SQUARESIZE*1.5:
			self.size = SQUARESIZE*1.5

		elif self.size < SQUARESIZE//2:
			self.size = SQUARESIZE//2


	def v_pos(self):
		return (self.x, self.y)

	def rowcol(self):
		return (self.row, self.col)

	def update(self):
		self.time -= 1

	def update_pos(self):
		x = self.x + random.randint(-1,1)
		y = self.y + random.randint(-1,1)
		return (x, y)



	def draw(self, screen):
		x, y = self.update_pos()
		rect = self.image.get_rect()
		rect.center = x, y

		screen.blit(self.image, (rect))
		# pygame.draw.circle(screen, SISTEMAS[self.sistema]['Color'], (self.x, self.y), int(self.size))

	def __str__(self):
		return ("Sistema afectado: {}. Tiempo restante: {}".format(SISTEMAS[self.sistema]['Nombre'], self.time))
