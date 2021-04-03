import random
import pygame
from vector import *
from config import *

class Agua(object):
	def __init__(self):
		self.color = (0,0,0)
		self.waterCount = 0
		self.waterHeight = 0
		self.colorA = random.randint(0,255)
		self.colorB = random.randint(0,255)
		self.colorC = random.randint(0,255)



	def update(self):
		if self.waterCount > WIDTH:
			self.waterHeight+=1
			self.waterCount = 0

		self.colorA += 0.05
		self.colorB += 0.1
		self.colorC += 0.15

		if self.colorA > 255:
			self.colorA = random.randint(0, 255)
		if self.colorB > 255:
			self.colorB = random.randint(0, 255)
		if self.colorC > 255:
			self.colorC = random.randint(0, 255)

		self.color = (int(self.colorA), int(self.colorB), int(self.colorC))


	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (0, HEIGTH-self.waterHeight, WIDTH, self.waterHeight))




class Gota(object):

	def __init__(self):
		self.x = random.randint(0, WIDTH)
		self.y = random.randint(-1000, 0)
		self.z = random.randint(0, 20)

		# self.xspeed = random.randint(-100, 100)/50
		self.xspeed = 0
		self.yspeed = random.random()
		self.zspeed = 0
		self.grav = self.z * 5 / 1000
		self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255), random.randint(0,255))
		# self.color = (255, 0, 0 )

		self.length = (self.z * 20 / 100) * 10
		self.width = (self.z * 3 / 100) 
		self.floor = (self.z * HEIGTH/2 / 100) + HEIGTH/2
		self.splash = False

	def build(self):
		self.y = random.randint(-500, -50)
		self.grav = self.z * 5 / 1000
		self.yspeed = 0.1
		self.zspeed = 0
		self.splash = False
		self.x = self.x = random.randint(0, WIDTH)
		self.xspeed = 0
		self.width = (self.z * 3 / 100) 

		# self.xspeed = random.randint(-100, 100)/50
		self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255), random.randint(0,255))



	def update(self):
		self.y += self.yspeed
		self.yspeed += self.grav
		self.x += self.xspeed
		if self.zspeed:
			self.z += self.zspeed
		self.width = (self.z * 20 / 100) * 10
		
		if self.width <= 0:
			self.width = 1
		print(self.width)
	


		if int(self.y) == int(self.floor):
			# self.color = (255, 255, 255)
			self.splash = True
		
		if self.y > HEIGTH:
			self.build()
			
	
	def draw(self, screen):
		# pygame.draw.line(screen, self.color, (int(self.x), int(self.y)), (int(self.x), int(self.y)+self.length), int(self.width))
		
		pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.width))

		# if self.splash:
		# 	pygame.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), int(self.width*15))
