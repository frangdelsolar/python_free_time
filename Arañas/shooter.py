from config import *
from bullet import *
import pygame

class Shooter():

	def __init__(self):
		self.x = WIDTH//2 - (WIDTH//5//2)
		self.y = HEIGTH - (HEIGTH//10)
		self.xspeed = 0
		self.yspeed = 0
		self.ancho = HEIGTH//25
		self.alto = HEIGTH//20

	def shoot(self):
		b = Bullet(self.x+self.ancho//2, self.y+self.alto//2)
		return b 


	def dir(self, x, y):
		self.xspeed = x
		self.yspeed = y


	def draw(self, screen):
		pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.ancho, self.alto))

	def update(self):
		self.x += self.xspeed
		self.y += self.yspeed

		if self.x <= 0 or self.x >= WIDTH-self.ancho:
			self.xspeed = 0

		
