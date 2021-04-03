from config import *
import pygame
import math

class Pacman():
	def __init__(self, row, col):
		self.start_row = row
		self.start_col = col
		self.row = row
		self.col = col
		self.x = col * SQUARESIZE + SQUARESIZE//2
		self.y = row * SQUARESIZE + SQUARESIZE//2
		self.color = (155, 155, 0)
		self.radius = SQUARESIZE//3
		self.xspeed = 0
		self.yspeed = 0
		self.lives = 3
		self.food_eaten = 0
		self.eaten_sound = pygame.mixer.Sound("sounds/pacman_death.wav")

	def die(self):
		self.play_eaten()
		self.lives -= 1
		self.y = self.start_row * SQUARESIZE + SQUARESIZE//2
		self.x = self.start_col * SQUARESIZE + SQUARESIZE//2
		self.xspeed = 0
		self.yspeed = 0


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
		# print(self.row, self.col)
		
		pygame.draw.rect(screen, (255,0,0), (self.col*SQUARESIZE, self.row*SQUARESIZE, SQUARESIZE, SQUARESIZE), 1)
		pygame.draw.circle(screen, (self.color), (self.x, self.y), self.radius)


		# pygame.draw.circle(screen, (self.color), (self.col*SQUARESIZE+SQUARESIZE//2, self.row*SQUARESIZE+SQUARESIZE//2), self.radius)

