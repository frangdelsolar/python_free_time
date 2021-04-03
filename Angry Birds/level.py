from config import *
from bird import Bird
from horquilla import Horquilla
from box import Box
from vector import Vector
import pygame
import random

class Level(object):
	def __init__(self):
		self.bird = None
		self.horquilla = None
		self.boxes = []
		self.build()

	def build(self):
		self.bird = Bird()
		self.horquilla = Horquilla()
		
		for i in range(1):
			self.boxes.append(Box())
		

	def update(self):
		self.bird.update()
		for box in self.boxes:
			box.update()		

	def draw(self, screen):
		self.bird.draw(screen)
		self.horquilla.draw(screen)
		self.horquilla.line(self.bird, screen)

		for box in self.boxes:
			box.draw(screen)