import pygame
import random
from config import *

class Car():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.xspeed = 0
		self.yspeed = 0
		self.xacc = 0
		self.yacc = 0
		self.incre = 0
		self.radius = int(SQUARESIZE*0.80//2)
		self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.row = int(self.y//SQUARESIZE)
		self.col = int(self.x//SQUARESIZE)
		self.state = 0
		self.timer = 0
		self.points = 0

	def teletransport(self, board):
		self.x =random.randint(0, width)
		self.y =random.randint(0, height)
		self.update(board)
		

	def piloto_automatico(self, board):

		for i in range(4):
			walls = []
			if board.grid[self.row][self.col].walls[i]:
				walls.append(i)

		for wall in walls:
			if wall == 0:
				self.yspeed = -1

			elif wall == 1:
				self.xspeed = 1

			if wall == 2:
				self.yspeed = 1

			elif wall == 3:
				self.xspeed = -1  

		self.update(board)



	def coord(self):
		return (self.x, self.y)

	def dir(self, direccion):
		self.xspeed = direccion[0] 
		self.yspeed = direccion[1] 
		self.xacc = direccion[0] * 0.01
		self.yacc = direccion[1] * 0.01


	def update(self, board):
		self.x += self.xspeed
		self.y += self.yspeed
		self.xspeed += self.xacc
		self.yspeed += self.yacc
		self.xacc += self.incre
		self.yacc += self.incre

		self.row = int(self.y//SQUARESIZE)
		self.col = int(self.x//SQUARESIZE)



		if self.state != 0:
			self.timer -= 1
			if self.timer% 50 ==0:
				self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
			if self.timer <= 0:
				self.state = 0

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
			if self.xspeed > 0:
				if board.grid[self.row][self.col].walls[1] or board.grid[self.row][self.col+1].walls[3]:
					if int(self.x+self.radius) >= int(board.grid[self.row][self.col+1].col*SQUARESIZE):
						self.xspeed = 0

			if self.xspeed < 0:
				if board.grid[self.row][self.col].walls[3] or board.grid[self.row][self.col-1].walls[1]:
					if int(self.x-self.radius) <= board.grid[self.row][self.col].col*SQUARESIZE:
						self.xspeed = 0

			if self.yspeed > 0:
				if board.grid[self.row][self.col].walls[2] or board.grid[self.row+1][self.col].walls[0]:
					if int(self.y+self.radius) >= board.grid[self.row][self.col].row*SQUARESIZE+SQUARESIZE:
						self.yspeed = 0

			if self.yspeed < 0:
				if board.grid[self.row][self.col].walls[0] or board.grid[self.row-1][self.col].walls[2]:
					if int(self.y-self.radius) <= board.grid[self.row][self.col].row*SQUARESIZE:
						self.yspeed = 0
		except:
			pass

	def draw(self, screen):
		myfont = pygame.font.SysFont("roboto", self.radius)	
		label = myfont.render(str(self.points), 1, (255,0,255))
					
		pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
		# pygame.draw.rect(screen, (255,0,0), (self.col*SQUARESIZE, self.row*SQUARESIZE, SQUARESIZE, SQUARESIZE), 1)

		screen.blit(label, (int(self.x-self.radius//2), int(self.y-self.radius//2)))

