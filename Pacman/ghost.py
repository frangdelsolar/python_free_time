from config import *
import pygame
import math
import random

class Ghost():
	def __init__(self, row, col, color):

		self.row = row
		self.col = col
		self.x = col *SQUARESIZE + SQUARESIZE//2
		self.y = row *SQUARESIZE + SQUARESIZE//2
		self.color = color
		self.radius = SQUARESIZE//3
		self.xspeed = 0
		self.yspeed = 0
		self.asustado = False
		self.susto_time = 0
		self.eaten_sound = pygame.mixer.Sound("sounds/pacman_eatghost.wav")

	def decide_where(self, pacman, board):

		paredes = board.grid[self.row][self.col].walls
		abiertas = []
		
		for p in paredes:
			pos = paredes.index(p)
			if not p:
				abiertas.append(pos)

		r = random.choice(abiertas)
		r = abiertas[-1]

		xs = 0
		ys = 0

		if r == 0:
			ys = -1
		
		elif r == 1:
			xs = 1
		
		elif r == 2:
			ys = 1
		
		elif r == 3:
			xs = -1

		print(xs, ys, self.x, self.y)
		return xs, ys


	def play_eaten(self):
		pygame.mixer.Sound.play(self.eaten_sound)
		pygame.mixer.music.stop()



	def dir(self, direccion):
		self.xspeed = direccion[0]
		self.yspeed = direccion[1]


	def update(self, board):

		self.x += self.xspeed 
		self.y += self.yspeed 
		self.row = self.y // SQUARESIZE
		self.col = self.x // SQUARESIZE


		if self.x <= 0 + SQUARESIZE//2: 
			self.xspeed = 0
			self.x = 0 + SQUARESIZE//2
		elif self.x >= width - SQUARESIZE//2: 
			self.xspeed = 0
			self.x = width - SQUARESIZE//2


		if self.y <= 0 + SQUARESIZE//2: 
			self.yspeed = 0
			self.y = 0 +SQUARESIZE//2
		elif self.y >= height - SQUARESIZE//2: 
			self.yspeed = 0
			self.y = height - SQUARESIZE//2

		
		try:			

			if self.col*SQUARESIZE == ((board.grid[self.row][self.col-1].col + 1) * SQUARESIZE):
				if self.xspeed == -1:
					if board.grid[self.row][self.col-1].walls[1] or board.grid[self.row][self.col].walls[3]:
							if self.x <= self.col*SQUARESIZE + SQUARESIZE//2:
								self.x = self.col*SQUARESIZE + SQUARESIZE//2
								self.xspeed = 0

				elif self.xspeed == 1:
					if board.grid[self.row][self.col+1].walls[3] or board.grid[self.row][self.col].walls[1]:
							if self.x >= self.col*SQUARESIZE + SQUARESIZE//2:
								self.x = self.col*SQUARESIZE + SQUARESIZE//2
								self.xspeed = 0

			if self.row*SQUARESIZE == (board.grid[self.row - 1][self.col].row + 1)*SQUARESIZE:
				if self.yspeed == - 1:
					if board.grid[self.row-1][self.col].walls[2] or board.grid[self.row][self.col].walls[0]:
							if self.y <= self.row*SQUARESIZE+ SQUARESIZE//2:
								self.y = self.row*SQUARESIZE+ SQUARESIZE//2
								self.yspeed = 0

				elif self.yspeed == 1:
					if board.grid[self.row+1][self.col].walls[0] or board.grid[self.row1][self.col].walls[2]:
							if self.y >= self.row*SQUARESIZE+ SQUARESIZE//2:
								self.y = self.row*SQUARESIZE+ SQUARESIZE//2
								self.yspeed = 0


		except:
			pass

	def draw(self, screen, board):
		self.update(board)

		if self.asustado:
			pygame.draw.circle(screen, (0,0,255), (self.x, self.y), self.radius)
		else:
			pygame.draw.circle(screen, (self.color), (self.x, self.y), self.radius)

		pygame.draw.rect(screen, (0,255,0), (self.col*SQUARESIZE, self.row*SQUARESIZE, SQUARESIZE, SQUARESIZE), 1)
