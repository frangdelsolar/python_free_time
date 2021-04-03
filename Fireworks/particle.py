import random
import pygame
from vector import *
from config import *

class Particle(object):

	def __init__(self, pos, firework, size):
		self.pos = pos
		self.firework = firework
		if firework:
			self.speed = [0, -(random.randint(7, 12))]
		else:
			coord = (random.randint(0, WIDTH), random.randint(0, HEIGTH))
			vector = Vector((self.pos[0], self.pos[1]), coord)
			nx, ny = vector.unit()
			r = random.randint(2,8)
			nx *= random.randint(1,random.randint(2,8))
			ny *= random.randint(1,random.randint(2,8))
			self.speed = [nx, ny]

		self.acc = [0, -0.1]
		self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255), random.randint(0,255))
		self.size = size


	def update(self, force):

		self.speed[0] += (self.acc[0] + force[0])
		self.speed[1] += (self.acc[1] + force[1])
		self.pos[0] += self.speed[0]
		self.pos[1] += self.speed[1]

		if not self.firework:
			self.speed[0] *= 0.95
			self.speed[1] *= 0.95
			self.size -= random.random()/10

	def pos(self):
		return (self.x, self.y)

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), int(self.size))