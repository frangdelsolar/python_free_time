from config import * 
import pygame
import random

class Bird(object):
	def __init__(self):
		self.x = 100
		self.y = 700
		self.xspeed = 0
		self.yspeed = 0
		self.xacc = 0.0001 
		self.yacc = 0
		self.gravedad = GRAVEDAD
		self.radius = 30

	def update(self):
		self.x += self.xspeed
		self.y += self.yspeed
		self.xspeed += self.xacc
		self.yspeed += self.yacc
		self.yspeed += self.gravedad

		# Si golpea el suelo
		if int(self.y + self.radius) > HEIGHT:
			if self.yspeed > 0:
				self.yspeed = self.yspeed * -0.9
			
				self.yacc = self.yacc *-0.9



	def draw(self, screen):
		pygame.draw.circle(screen, (200, 0, 0), (int(self.x), int(self.y)), self.radius)
