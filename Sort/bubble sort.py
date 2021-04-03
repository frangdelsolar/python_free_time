import random
import pygame
import sys


WIDTH = 900
HEIGTH = 600
SCREEN_SIZE = (WIDTH, HEIGTH)
LINE_WIDTH = 1
SQUARESIZE = WIDTH//100

MP = WIDTH
MH = HEIGTH



class Line():
	def __init__(self, x, heigth):
		self.x = x
		self.heigth = heigth
		self.width = LINE_WIDTH

	def draw(self, screen):

		# pygame.draw.rect(screen, DARK_GREY, (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))
		pygame.draw.rect(screen, (255,255,255), (self.x, HEIGTH-self.heigth, self.width, self.heigth))

class Elements():
	MP = WIDTH
	MH = HEIGTH
	def __init__(self):
		self.lines = []
		self.build()


	def build(self):
		for i in range(WIDTH//LINE_WIDTH):
			x = random.randint(0, WIDTH)
			heigth = random.randint(0, HEIGTH)
			line = Line(x, heigth)
			self.lines.append(line)

	def draw(self, screen):
		for l in self.lines:
			l.draw(screen)

	
	def bubbleSort(self):

		count = 0	
		for i in range (2, len(self.lines):
			if self.lines[i].heigth < self.lines[i+1].heigth:
				aux = self.lines[i].heigth
				self.lines[i].heigth = self.lines[i+1].heigth
				self.lines[i+1].heigth = aux
				
				pygame.display.update()
				count += 1
				return count

	

	def miAlgo(self):

		for i in range(0, WIDTH):
			if MH > self.lines[i].heigth:
				MH = self.lines[i].heigth
				MP = self.lines[i].x

		print(MP, MH)
		# self.lines[i].heigth = mh
		# mh = aux
		# pygame.display.update()




		


def play():

	pygame.init()
	e = Elements()
	go = True



	while go:
		
		screen = pygame.display.set_mode(SCREEN_SIZE)

		e.draw(screen)
		pygame.display.update()

		if e.bubbleSort() == 0:
			break

		# if e.miAlgo() == 0:
		# 	break


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

play()