from config import *
import pygame
import random


class Brick():
	def __init__(self, row, col):

		self.row = row
		self.col = col
		self.points = 10
		self.font = pygame.font.SysFont("roboto", SQUARESIZE//2)
		self.x = col*SQUARESIZE
		self.y = row*SQUARESIZE
		self.color = (200,200,200)


	def check_hit(self, projectiles):
		for p in projectiles:			
			
			# Resta puntos si la bola toca el brick
			if self.row == p.row and self.col == p.col:
				self.points -= 1
				self.color = (255,0,0)


				if int(p.x) == int(self.x): 
					p.xspeed = p.xspeed *-1
					p.xacc = p.xacc* -1
					self.color = (200,200,200)

				elif int(p.x) == int(self.x+SQUARESIZE//2):
					p.xspeed = p.xspeed *-1
					p.xacc = p.xacc* -1
					self.color = (200,200,200)

				if int(p.y) == int(self.y):
					p.yspeed = p.yspeed *-1
					p.yacc = p.yacc* -1
					self.color = (200,200,200)

				elif int(p.y) == int(self.y+SQUARESIZE//2):
					p.yspeed = p.yspeed *-1
					p.yacc = p.yacc* -1
					self.color = (200,200,200)
	


	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (self.col*SQUARESIZE, self.row*SQUARESIZE, SQUARESIZE, SQUARESIZE))
		pygame.draw.rect(screen, (100,100,100), (self.col*SQUARESIZE, self.row*SQUARESIZE, SQUARESIZE, SQUARESIZE), 1)

		label = self.font.render(str(self.points), 1, BLACK)
		screen.blit(label, (int(self.col*SQUARESIZE+SQUARESIZE/4), int(self.row*SQUARESIZE+ SQUARESIZE/4)))


