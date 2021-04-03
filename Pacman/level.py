from config import *
from board import *
from food import *
from pacman import *
from ghost import *
import pygame
import sys
import math


class Level():
	
	def __init__(self):
		
		self.board = Board(size)
		self.food = []
		self.fruit = []
		self.pacman = Pacman(random.randint(0, size-1), random.randint(0, size-1))		
		self.ghosts = []
		self.sound = pygame.mixer.Sound("sounds/pacman_beginning.wav")
		self.build()
		self.sembrar()
		self.ghostize()

	def move_ghosts(self):
		for g in self.ghosts:
			direccion = g.decide_where(self.pacman, self.board)
			g.dir(direccion)



	def check_win(self):
		if self.pacman.food_eaten == self.board.size * self.board.size:
			return True
		return False
		

	def check_over(self):
		if self.pacman.lives == 0:
			return True
		return False

	def ghostize(self):
		for i in range(size//4):
			r = random.randint(0, size)
			c = random.randint(0, size)
			color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
			g = Ghost(r, c, color)
			self.ghosts.append(g)


	def sembrar(self):
		for r in range(self.board.size):
			for c in range(self.board.size):
				f = Food(r, c)
				self.food.append(f)

		for i in range(self.board.size):
			r1 = random.randint(0, self.board.size)
			r2 = random.randint(0, self.board.size)
			fr = Fruit(r1, r2)
			self.fruit.append(fr)


	def update(self):

		for f in self.food:
			if self.pacman.row == f.row and self.pacman.col == f.col:
				f.eat_sound()
				pos = self.food.index(f)
				self.food.pop(pos)
				self.pacman.food_eaten += 1

		for fr in self.fruit:
			if self.pacman.row == fr.row and self.pacman.col == fr.col:
				fr.eat_sound()
				pos = self.fruit.index(fr)
				self.fruit.pop(pos)
				for g in self.ghosts:
					g.asustado = True
					g.susto_time = 1000

		for g in self.ghosts:
			if self.pacman.row == g.row and self.pacman.col == g.col:
				if g.asustado:
					g.play_eaten()
					pos = self.ghosts.index(g)
					self.ghosts.pop(pos)
				else:
					self.pacman.die()
			direccion = g.decide_where(self.pacman, self.board)
			g.dir(direccion)



					

	def draw(self, screen):

		self.update()

		for r in range(self.board.size):
			for c in range(self.board.size):
				self.board.grid[r][c].draw_grey(screen)

		for f in self.food:
			f.draw(screen)

		for fr in self.fruit:
			fr.draw(screen)

		for g in self.ghosts:
			g.draw(screen, self.board)

		self.pacman.draw(screen, self.board)


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
		
		# pygame.mixer.Sound.play(self.sound)
    	
	
		all_visited = False

		pygame.init()
		pygame.display.set_caption('Maze generator')

		clock = pygame.time.Clock()

		current = self.board.grid[0][0]

		stack = []
		
		while not all_visited:

			screen = pygame.display.set_mode(screen_size)
			self.board.draw(screen, current)

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

		pygame.mixer.music.stop()

			

				
