import random
import pygame
import math
import sys

GENTE = 10

GREY = (220, 220, 220)
DARK_GREY = (169, 169, 169)
GREEN = (11, 102, 35)
RED = (255, 0,0)
TURQUESA = (135, 206, 235)
BLACK = (0, 0, 0)

RADIUS = 3

SQUARESIZE = 50
SQUARES = 16
height = SQUARESIZE*SQUARES
width = SQUARESIZE*SQUARES
screen_size = (800, 800)



class Screen():
	def __init__(self):
		self.grid = [[[]]*SQUARES for i in range(SQUARES)]

	def show(self):
		for i in range(16):
			for j in range(16):
				print(len(self.grid[i][j]) , end= "  ")
			print()


GRID = Screen()
	# def update(self, grupo):
	# 	for i in range(SQUARES):
	# 		for j in range(SQUARES):
	# 			for k in grupo.gente:
	# 				if k.row ==i and k.col ==j:
	# 					self.grid[i][j].append(k)







class Vector():
	def __init__(self, list1, list2):
		self.diff = (list2[0]-list1[0], list2[1]-list1[1])


	def distance(self):
		self.a = self.diff[0]
		self.b = self.diff[1]
		return math.sqrt(self.a**2 + self.b**2)

	def unit(self):
		distance = self.distance()
		if distance != 0:
			self.aunit = self.a/distance
		else:
			self.aunit = 0

		if distance != 0:
			self.bunit = self.b/distance
		else:
			self.bunit = 0
		return self.aunit, self.bunit 

	def add(self, one, two):
		self.sum =(one[0]+two[0], one[1]+two[1])
		return self.sum

	def multiply(self, v, num):
		self.product =(v[0]*num, v[1]*num)
		return self.product



class Persona():
	def __init__(self, x, y, color):
		self.x = x 
		self.y = y
		self.row = int(math.floor(self.x/SQUARESIZE))
		self.col = int(math.floor(self.y/SQUARESIZE))
		self.xspeed = 0
		self.yspeed = 0
		self.color = color
		self.size = RADIUS
		self.vecinos = []
	
	def coord(self):
		return (self.x, self.y)

	def juntarse(self, lider):
		s_pos = (self.x, self.y)
		l_pos = (lider.x, lider.y)

		v = Vector(s_pos, l_pos)
		nx, ny = v.unit()

		if v.distance() < (RADIUS*2 + 1):
			nx = 0
			ny = 0

		self.xspeed = nx
		self.yspeed = ny


	def update(self):
		self.x += self.xspeed
		self.y += self.yspeed
		self.row = int(math.floor(self.x/SQUARESIZE))
		self.col = int(math.floor(self.y/SQUARESIZE))
		
		if not self in GRID.grid[self.row][self.col]:
			GRID.grid[self.row][self.col].append(self)

		

		# try:
			

		# except:
		# 	pass

	def show(self, screen):
		pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

class Group():
	def __init__(self, name, color):
		self.name = ''
		self.gente = []
		self.color = color
		self.build()
		self.liderar()
		# self.centrar_leader()


	def liderar(self):
		lider = self.gente[0]
		lider.size = RADIUS*3
		lider.color = BLACK
		

		for p in self.gente:
			if p != lider:
				if not p in lider.vecinos:
					if p.row==lider.row and p.col==lider.col:
						lider.vecinos.append(p)

		for v in lider.vecinos:
			vector = Vector(v.coord(), lider.coord())
			if vector.distance() > 50:
				i = lider.vecinos.index(v)
				lider.vecinos.pop(i)
		

		# for v in lider.vecinos:
		# 	v.juntarse(lider)
	

	def dir(self, x, y):
		lider = self.gente[0]
		lider.x_velocity = x
		lider.y_velocity = y	


	def build(self):
		for i in range(GENTE):
			p = Persona(random.randint(0, width), random.randint(0, height), self.color)
			self.gente.append(p)

	def update(self):
		self.liderar()
		for p in self.gente:
			p.update()


	def show(self, screen):
		for p in self.gente:
			p.show(screen)

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

		GRID.show()
		# s.update(g)


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