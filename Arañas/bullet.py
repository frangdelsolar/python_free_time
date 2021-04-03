import pygame 
import random

class Bullet():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.xspeed = 0
		self.yspeed = -(random.randint(1,10))
		self.power = -(random.randint(1,5))
		self.size = abs(self.power)

	def update(self):
		self.x += self.xspeed
		self.y += self.yspeed


	def draw(self, screen):
		pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), self.size)
