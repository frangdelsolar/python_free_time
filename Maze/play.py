from config import *
from user import *

from board import *
import pygame
import sys
import math

def removeWalls(a, b):
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



def play():
	

	board = Board(size)
	all_visited = False

	pygame.init()
	pygame.display.set_caption('Maze generator')

	clock = pygame.time.Clock()

	current = board.grid[0][0]

	stack = []
	
	while not all_visited:

		screen = pygame.display.set_mode(screen_size)
		board.draw(screen, current)

		current.visited = True
		
		pygame.display.update()


		# Step 1
		vecino = current.check_vecinos()

		if vecino:
			vecino.visited = True

			# Step 2
			stack.append(current)

			#Step 3
			removeWalls(current, vecino)

			# Step 4
			current = vecino

		elif len(stack) > 0:
			current.marcada = True
			cell = stack.pop(-1)
			current = cell


		clock.tick(1000)

		if not vecino and len(stack)==0 and current == board.grid[0][0]:


			# Re draw
			current = None
			


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
play()
