from config import *
from board import *

import pygame
import sys
import math
from car import Car
from fuel import Fuel, Nitro


class Level():
	
	def __init__(self):
		
		self.board = Board(size)
		self.cars = []
		self.fuel = []
		self.nitro = []
		self.build()
		self.regar()

	def update(self):

		# self.cars[1].piloto_automatico(self.board)

		for car in self.cars:

			for f in self.fuel:
				if car.row == f.row and car.col == f.col:
					pos = self.fuel.index(f)
					self.fuel.pop(pos)
					car.points += 1


			for ni in self.nitro:
				if car.row == ni.row and car.col == ni.col:
					pos = self.nitro.index(ni)
					self.nitro.pop(pos)
					car.points += 3
					car.incre *= 1.10

					for cother in self.cars:
						if car != cother:
							cother.state = 1
							cother.timer = 3000



	def regar(self):
		for r in range(self.board.size):
			for c in range(self.board.size):
				f = Fuel(r, c)
				self.fuel.append(f)

		for i in range(self.board.size):
			r1 = random.randint(0, self.board.size)
			r2 = random.randint(0, self.board.size)
			ni = Nitro(r1, r2)
			self.nitro.append(ni)

	def draw(self, screen):

		for r in range(self.board.size):
			for c in range(self.board.size):
				self.board.grid[r][c].draw_grey(screen, self.cars)

		for f in self.fuel:
			f.draw(screen)

		for n in self.nitro:
			n.draw(screen)

		for car in self.cars:
			car.update(self.board)
			car.draw(screen)


	def removeWalls(self, a, b):
		x = a.col - b.col
		if x == 1:
			a.walls[3] = False
			b.walls[1] = False
		elif x == -1:
			a.walls[1] = False
			b.walls[3] = False

		y = a.row - b.row
		if y == 1:
			a.walls[0] = False
			b.walls[2] = False
		elif y == -1:
			a.walls[2] = False
			b.walls[0] = False

	def build(self):		  	
	
		all_visited = False

		pygame.init()
		pygame.display.set_caption('Maze generator')

		clock = pygame.time.Clock()

		current = self.board.grid[0][0]

		stack = []
		
		while not all_visited:

			screen = pygame.display.set_mode(screen_size)
			self.board.draw(screen, current, self.cars)

			current.visited = True
			
			pygame.display.update()


			# Step 1
			vecino = current.check_vecinos()

			if vecino:
				vecino.visited = True

				# Step 2
				stack.append(current)

				#Step 3
				self.removeWalls(current, vecino)

				# Step 4
				current = vecino

			elif len(stack) > 0:
				current.marcada = True
				cell = stack.pop(-1)
				current = cell


			clock.tick(10000)

			if not vecino and len(stack)==0 and current == self.board.grid[0][0]:
				break

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()


		car1= Car(width-30, height//2-30)
		car2= Car(width-30, height//2+30)

		self.cars.append(car1)
		self.cars.append(car2)

		pygame.mixer.music.stop()

			

				
