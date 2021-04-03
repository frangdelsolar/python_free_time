from config import *
import pygame



class Cell(object):
	
	def __init__(self):
		self.row = 0
		self.col = 0
		self.value = 0
		self.is_revealed = False
		self.placeholder = "."
		self.vecindad = []
		self.img = ''

	def revelar_vecinos(self, screen):
		self.draw(screen)
		pygame.display.update()
		for v in self.vecindad:
			v.draw(screen)
			pygame.display.update()
			if not v.is_revealed:

				v.revelar_vecinos(screen)
	
	def show(self):
		print("({}, {}). Mi valor es {} y he sido revelada {}".format(self.row, self.col, self.value, self.is_revealed))

	def draw(self, screen):

		myfont = pygame.font.SysFont("monospace", FONTSIZE)
		myfont.set_bold(True)
		
		if self.is_revealed == True:

					if self.value == 0:
						pygame.draw.rect(screen, GREY, (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))

					elif self.value == "@":

						pygame.draw.rect(screen, RED, (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))
						mineimg = pygame.image.load('img/ghost.png')
						mineimg = pygame.transform.scale(mineimg, (SQUARESIZE, SQUARESIZE))
						screen.blit(mineimg, (self.col * SQUARESIZE, self.row * SQUARESIZE))

					else:
						pygame.draw.rect(screen, DARK_GREY, (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))
						label = myfont.render(str(self.value), 1, BLACK)
						screen.blit(label, (int(self.col*SQUARESIZE+SQUARESIZE/3), int(self.row*SQUARESIZE+ SQUARESIZE/3)))

					pygame.draw.rect(screen, (120, 120, 120), (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE),1)

		elif self.is_revealed == False:
			if self.placeholder == "P":
				pygame.draw.rect(screen, GREEN, (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))

				flagimg = pygame.image.load('img/ghost.png')
				flagimg = pygame.transform.scale(flagimg, (SQUARESIZE, SQUARESIZE))

				screen.blit(flagimg, (self.col * SQUARESIZE, self.row * SQUARESIZE))

			
			if self.placeholder == ".":
				pygame.draw.rect(screen, (100, 100, 100), (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE))
			
			pygame.draw.rect(screen, (50, 50, 50), (self.col * SQUARESIZE, self.row * SQUARESIZE, SQUARESIZE, SQUARESIZE),1)
