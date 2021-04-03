import pygame 
from config import *


class Cell():
	def __init__(self):
		self.value = " "
		self.regla = ""
		self.posicion = 0
		self.row = None
		self.col = None

	def draw(self, screen):
		myfont = pygame.font.SysFont("roboto", 25)
		myfont.set_bold(False)


		if self.regla == 'TW':
			pygame.draw.rect(screen, ORANGE, (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))
		
		elif self.regla == 'DL':
			pygame.draw.rect(screen, BLUE, (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))
		
		elif self.regla == 'DW':
			pygame.draw.rect(screen, RED, (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))
		
		elif self.regla == 'TL':
			pygame.draw.rect(screen, GREEN, (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))

		else:
			pygame.draw.rect(screen, GREY, (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))

		pygame.draw.rect(screen, DARK_GREY, (self.col*SQUARESIZE, self.row*SQUARESIZE, SQUARESIZE, SQUARESIZE), 3)

		if self.regla:
			label = myfont.render(str(self.regla), 1, BLACK)
			screen.blit(label, (int(self.col*SQUARESIZE+SQUARESIZE/3), int(self.row*SQUARESIZE+ SQUARESIZE/3)))


class Board():
	def __init__(self):
		self.board=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
		
		self.board_rules=[['TW', 0, 0, 'DL', 0, 0, 0, 'TW', 0, 0, 0, 'DL', 0, 0, 'TW'],
						  [0, 'DW', 0, 0, 0, 'TL', 0, 0, 0, 'TL', 0, 0, 0, 'DW', 0],
						  [0, 0, 'DW', 0, 0, 0, 'DL', 0, 'DL', 0, 0, 0, 'DW', 0, 0],
						  ['DL', 0, 0, 'DW', 0, 0, 0, 'DL', 0, 0, 0, 'DW', 0, 0, 'DL'],
						  [0, 0, 0, 0, 'DW', 0, 0, 0, 0, 0, 'DW', 0, 0, 0, 0],
						  [0, 'TL', 0, 0, 0, 'TL', 0, 0, 0, 'TL', 0, 0, 0, 'TL', 0],
						  [0, 0, 'DL', 0, 0, 0, 'DL', 0, 'DL', 0, 0, 0, 'DL', 0, 0],
						  ['TW', 0, 0, 'DL', 0, 0, 0, 0, 0, 0, 0, 'DL', 0, 0, 'TW'],
						  [0, 0, 'DL', 0, 0, 0, 'DL', 0, 'DL', 0, 0, 0, 'DL', 0, 0],
						  [0, 'TL', 0, 0, 0, 'TL', 0, 0, 0, 'TL', 0, 0, 0, 'TL', 0],
						  [0, 0, 0, 0, 'DW', 0, 0, 0, 0, 0, 'DW', 0, 0, 0, 0],
						  ['DL', 0, 0, 'DW', 0, 0, 0, 'DL', 0, 0, 0, 'DW', 0, 0, 'DL'],
						  [0, 0, 'DW', 0, 0, 0, 'DL', 0, 'DL', 0, 0, 0, 'DW', 0, 0],
						  [0, 'DW', 0, 0, 0, 'TL', 0, 0, 0, 'TL', 0, 0, 0, 'DW', 0],
						  ['TW', 0, 0, 'DL', 0, 0, 0, 'TW', 0, 0, 0, 'DL', 0, 0, 'TW']]
		self.fichas = []
		self.build()

	def build(self):
		posicion = 0
		for i in range(15):
			for j in range(15):
				c = Cell()
				c.row = i
				c.col = j
				c.posicion = posicion
				c.regla = self.board_rules[i][j]
				self.board[i][j] = c
				posicion += 1

	
	def draw(self, screen):
		for r in range(len(self.board)):
			for c in range(len(self.board)):
				self.board[r][c].draw(screen)

		for f in self.fichas:
			f.draw(screen)

	
	def show(self):
		print (" -----------------------------------------------------------------------------------------")
		for i in range(15):
			for j in range(15):

				if self.board[i][j].posicion >= 100 and self.board[i][j].posicion < 1000:
					print("|", self.board[i][j].posicion, end=" ")

				if self.board[i][j].posicion >= 10 and self.board[i][j].posicion < 100:
					print("| ", self.board[i][j].posicion, end=" ")

				if self.board[i][j].posicion >= 0 and self.board[i][j].posicion < 10:
					print("| ", self.board[i][j].posicion, end="  ")

			print("|")
			print(" -----------------------------------------------------------------------------------------")

	