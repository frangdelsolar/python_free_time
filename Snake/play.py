# from snake import Snake
import pygame
import sys
import random


clock = pygame.time.Clock()
scl = 20
width = 600
height = 600
GREY = (220, 220, 220)
GREEN = (0, 255, 0)
RED = (255,0,0)


def constrain(pos, inicio, fin):
	if pos <= inicio:
		return inicio

	elif pos >= fin:
		return (fin-scl)

	return pos

class Snake():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.xspeed = 1
		self.yspeed = 0
		self.total = 0
		self.tail = []


	def dir(self, x, y):
		self.xspeed = x
		self.yspeed = y

	def update(self, screen):
		
		for i in range(self.total):
			self.tail.append((self.x, self.y))

		self.x += self.xspeed * scl
		self.x = constrain(self.x, 0, width)
		self.y += self.yspeed * scl
		self.y = constrain(self.y, 0, height)
		
		print(self.tail)


	def show(self, screen):
		
		for i in self.tail:
			x, y = i
			pygame.draw.rect(screen, RED, (x, y, scl, scl))
			x += scl
			y += scl

		pygame.draw.rect(screen, GREY, (self.x, self.y, scl, scl))

def pickLocation():
	cols = width//scl
	rows = height//scl
	food_loc = (random.randint(0, cols), random.randint(0, rows))
	return food_loc

def eat(snake, foodx, foody):
	foodx *= scl
	foody *= scl
	if snake.x == foodx and snake.y == foody:
		return True
	return False


def play():

	pygame.init()
	screen_size = (width, height)
	screen = pygame.display.set_mode(screen_size)

	s = Snake()
	s.show(screen)
	pygame.display.update()
	fx, fy = pickLocation()	
	game_over = False
	
	while game_over == False:

		tic = clock.tick(10)

		screen = pygame.display.set_mode(screen_size)


		s.tail = []
		s.update(screen)
		s.show(screen)

		
		if eat(s, fx, fy):
			fx, fy = pickLocation()
			s.total += 1

		food = pygame.draw.rect(screen, GREEN, (fx*scl, fy*scl, scl, scl))
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					s.dir(0, 1)
				if event.key == pygame.K_UP:
					s.dir(0, -1)
				if event.key == pygame.K_LEFT:
					s.dir(-1, 0)
				if event.key == pygame.K_RIGHT:
					s.dir(1, 0)



play()