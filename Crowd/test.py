import random
import pygame
import math
import sys

GREY = (220, 220, 220)

DARK_GREY = (169, 169, 169)

GREEN = (11, 102, 35)
RED = (255, 0,0)
TURQUESA = (135, 206, 235)
BLACK = (0, 0, 0)

RADIUS = 3


height = 800
width = 800
screen_size = (width, height)

class Persona():
	def __init__(self, x, y, xspeed, yspeed, color):
		self.x = x 
		self.y = y
		self.x_velocity = xspeed
		self.y_velocity = yspeed
		self.dir = 0
		self.color = color

	def juntarse(self, lider):
		print("1. x", self.x, self.y,  lider.x, lider.y)
		
		if self.x < lider.x:
			self.x += 1
		elif self.x == lider.x:
			self.x += 0
		else:
			self.x += -1

		if self.y < lider.y:
			self.y += 1
		elif self.y == lider.y:
			self.y += 0
		else:
			self.y += -1

		print("2. x", self.x, self.y,  lider.x, lider.y)




	def update(self):
		try:
			self.x += self.x_velocity
			self.y += self.y_velocity
		except:
			pass

	def show(self, screen):
		pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), RADIUS)

class Group():
	def __init__(self, name, color):
		self.name = ''
		self.gente = []
		self.color = color
		self.build()
		self.centrar_leader()

	def centrar_leader(self):
		lider = self.gente[0]
		lider.color = BLACK
		lider.x = width//2
		lider.y = height//2
		lider.x_velocity = 0
		lider.y_velocity = 0
		

		for i in range(1, len(self.gente)):
			self.gente[i].juntarse(lider)

	def dir(self, x, y):
		lider = self.gente[0]
		lider.x_velocity = x
		lider.y_velocity = y
		


	def build(self):
		for i in range(2):
			p = Persona(random.randint(0, width), random.randint(0, height), random.randint(-1, 1), random.randint(-1, 1), self.color)
			self.gente.append(p)

	def update(self):
		self.centrar_leader()
		for p in self.gente:
			p.update()

	def show(self, screen):
		for p in self.gente:
			p.show(screen)



def constrain(speed):
	print(speed)
	if speed == 0:
		return(random.choice([-1, 1]))
	if speed > 5:
		return 5
	elif speed < -5:
		return -5

def play():

	game_over = False

	pygame.init()
	
	screen = pygame.display.set_mode(screen_size)
	screen.fill(GREY)
	pygame.display.update()

	g = Group('Fighters', RED)


	counter = 0

	while not game_over:

		screen = pygame.display.set_mode(screen_size)
		screen.fill(GREY)


		g.show(screen)
		g.update()


		pygame.display.update()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_DOWN:
					g.dir(0, 1)
				if event.key == pygame.K_UP:
					g.dir(0, -1)
				if event.key == pygame.K_LEFT:
					g.dir(-1, 0)
				if event.key == pygame.K_RIGHT:
					g.dir(1, 0)
			
			# if event.type == pygame.MOUSEMOTION:

			# 	print(event.rel)

			# 	x_speed = constrain(event.rel[0])
			# 	y_speed = constrain(event.rel[1])


			# 	g.dir(x_speed, y_speed)

			# 	# if event.rel[1] > 0:
			# 	# 	g.dir(0, 2)
			# 	# if event.rel[1] < 0:
			# 	# 	g.dir(0, -2)
				
			# 	# if event.rel[0] < 0:
			# 	# 	g.dir(-2, 0)
			# 	# if event.rel[0] > 0:
			# 	# 	g.dir(2, 0)
		counter+=1

play()