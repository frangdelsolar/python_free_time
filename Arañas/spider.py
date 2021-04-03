from config import *
import pygame
import random

class Spider():

	def __init__(self):
		self.x = random.randint(30, WIDTH-30)
		self.y = random.randint(HEIGTH//10, (HEIGTH//3)*2)
		self.xspeed = 0
		self.yspeed = random.random()
		self.ybottom = (HEIGTH//3)*2
		self.size = random.randint(10, 70)
		self.image = pygame.image.load('img/spider.png')
		self.color = random.randint(150, 200)
		self.xcopy = self.x

	def draw(self, screen):
		self.image = pygame.transform.scale(self.image, (int(self.size), int(self.size*3)))
		pygame.draw.line(screen, (self.color, self.color, self.color), (self.xcopy, 0), (self.x, self.y))
		rect = self.image.get_rect()
		rect.center = self.x, self.y
		screen.blit(self.image, (rect))

	def update(self):
		# self.xspeed = random.randint(-1, 1)

		if self.y >= self.ybottom:
			self.yspeed = -(random.random())

		if self.y <= HEIGTH//10:
			self.yspeed = (random.random())

		self.y += self.yspeed

		self.ybottom += 0.01


		self.x += self.xspeed
		