from config import *
import pygame

class Horquilla(object):
	def __init__(self):
		self.length = SQ * 4
		self.width = SQ // 3
		self.x = WIDTH // 4
		self.y = HEIGHT-self.length

	def line(self, bird, screen):
		pygame.draw.line(screen, (255,255,155), (self.x, self.y+10), (bird.x, bird.y), 2)		

	def draw(self, screen):
		pygame.draw.line(screen, (250,250,250), (self.x, self.y), (self.x, HEIGHT), self.width)