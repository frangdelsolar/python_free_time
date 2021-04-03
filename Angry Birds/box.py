from config import *
import pygame
import random

class Box(object):
	def __init__(self):
		self.size = SQ*3
		self.x = WIDTH - SQ*5
		self.y = HEIGHT - self.size
		self.xspeed = 0
		self.yspeed = 0
		self.xacc = 0 
		self.yacc = 0
		self.gravedad = GRAVEDAD
		

	def update(self):
		# Si golpea el suelo
		if int(self.y + self.size) > HEIGHT:
			if self.yspeed > 0:
				self.yspeed = self.yspeed * -1
				self.yacc = self.yacc * -1
			# self.gravedad = 0
			# self.yacc = self.yacc * -1
			# if self.yspeed < 0.1 and self.yacc == 0:
			# 	self.yspeed = 0

		self.x += self.xspeed
		self.y += self.yspeed
		self.xspeed += self.xacc
		self.yspeed += (self.yacc + self.gravedad)

		print(int(self.y), self.yspeed, self.yacc)
			

	def draw(self, screen):
		pygame.draw.rect(screen, (100, 100, 100), (int(self.x), int(self.y), self.size, self.size))