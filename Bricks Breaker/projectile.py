from config import *
import pygame
import random


class Projectile():
	def __init__(self):
		self.radius = 10
		# self.x = width//2
		# self.y = height - self.radius*2
		self.x = random.randint(0+self.radius, width-self.radius)
		self.y = random.randint(0+self.radius, height-self.radius)
		self.xspeed = 0
		self.yspeed = 0
		self.xacc = 0
		self.yacc = 0
		self.row = self.y//SQUARESIZE
		self.col = self.x//SQUARESIZE

	def coord(self):
		return (self.x, self.y)

	def draw(self, screen):
		pygame.draw.circle(screen, (0,255,0), (int(self.x), int(self.y)), self.radius)
		# pygame.draw.rect(screen, (255,0,0), (self.col*SQUARESIZE, self.row*SQUARESIZE, SQUARESIZE, SQUARESIZE), 1)

	def update(self):
		self.x += self.xspeed
		self.y += self.yspeed
		self.xspeed += self.xacc
		self.yspeed += self.yacc

		self.row = self.y//SQUARESIZE
		self.col = self.x//SQUARESIZE

		# Rebotar en las paredes
		if int(self.x - self.radius) <= 0: 
			self.xspeed = -self.xspeed
			self.xacc += ACCELERATION
		
		elif int(self.x + self.radius) >= height:
			self.xspeed = -self.xspeed
			self.xacc += -ACCELERATION

		# Rebotar en el techo
		if int(self.y - self.radius) <= 0:
			self.yspeed = -self.yspeed
			self.yacc += ACCELERATION

		# Detenerse en el suelo
		elif int(self.y + self.radius) >= width:
			self.xspeed = 0
			self.yspeed = 0
			self.xacc = 0
			self.yacc = 0

		
		# Constrain speed
		if int(self.xspeed) >= SPEED_LIMIT:  
			self.xspeed = SPEED_LIMIT
		elif int(self.xspeed) <= -SPEED_LIMIT:  
			self.xspeed = -SPEED_LIMIT

		if int(self.yspeed) >= SPEED_LIMIT:  
			self.yspeed = SPEED_LIMIT
		elif int(self.yspeed) <= -SPEED_LIMIT:  
			self.yspeed = -SPEED_LIMIT
		



