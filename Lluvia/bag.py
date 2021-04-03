import random
import pygame
from vector import *
from config import *

class Bag(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.size = 10

	def update(self, x, y):
		self.x = x
		self.y = y


	def draw(self, screen):
		pygame.draw.circle(screen, (200, 200, 200), (self.x, self.y), int(self.size))