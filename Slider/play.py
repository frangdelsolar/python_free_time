import pygame
import random
import sys


GRID_SIZE = 5
width = 900
height = 900

SQUARE_SIZE = width //  GRID_SIZE
FONT_SIZE = SQUARE_SIZE//2


GREY = (220,220,220)
MIDDLE_GREY = (200, 200, 200)
DARK_GREY = (169, 169, 169)
BLACK = (0, 0, 0)
# BLUE = (0, 0, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)





class Board():
	def __init__(self):
		self.grid =[[0] * GRID_SIZE  for i in range(GRID_SIZE)]
		self.build()

	def build(self):
		nums = []
		
		for i in range(0, GRID_SIZE*GRID_SIZE):
			nums.append(i)


		for i in range(GRID_SIZE):
			for j in range(GRID_SIZE):

				randChoice = random.choice(nums)
				self.grid[i][j] = randChoice

				index = nums.index(randChoice)
				nums.pop(index)



	def buscar_cero(self):
		for r in range(GRID_SIZE):
			for c in range(GRID_SIZE):
				if self.grid[r][c] == 0:
					return (r, c)			 	

	def check_win(self):

		orden_ideal = []

		for i in range(1, GRID_SIZE*GRID_SIZE):
			orden_ideal.append(i)

		orden_ideal.append(0)


		orden_real = []
		for r in range(0, GRID_SIZE):
			for c in range(GRID_SIZE):
				orden_real.append(self.grid[r][c])

		for j in range(0, GRID_SIZE*GRID_SIZE):
			if orden_ideal[j] != orden_real[j]:
				return False
		return True


	def cero_arriba(self, cero):
		r, c = cero
		try:
			if r != GRID_SIZE:
				if self.grid[r+1][c] != 0:
					self.grid[r][c] = self.grid[r+1][c]
					self.grid[r+1][c] = 0
		except:
			pass

	def cero_abajo(self, cero):
		r, c = cero
		try:
			if r != 0:
				if self.grid[r-1][c] != 0:
					self.grid[r][c] = self.grid[r-1][c]
					self.grid[r-1][c] = 0
		except:
			pass

	def cero_derecha(self, cero):
		r, c = cero
		try:
			if c != 0:
				if self.grid[r][c-1] != 0:
					self.grid[r][c] = self.grid[r][c-1]
					self.grid[r][c-1] = 0
		except:
			pass


	def cero_izquierda(self, cero):
		r, c = cero
		try:
			if c != GRID_SIZE:
				if self.grid[r][c+1] != 0:
					self.grid[r][c] = self.grid[r][c+1]
					self.grid[r][c+1] = 0
		except:
			pass
 


	def show(self, screen):
		# for i in self.grid:
		# 	print(i)

		for r in range(GRID_SIZE):
			for c in range(GRID_SIZE):

				myfont = pygame.font.SysFont("roboto", FONT_SIZE)

				# Implementar función de que si la celda está junto al cero, las letras se ponen verdes
				
				if self.grid[r][c] != 0:
					pygame.draw.rect(screen, GREY, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
					label = myfont.render(str(self.grid[r][c]), 1, BLACK)
					screen.blit(label, (int(c*SQUARE_SIZE+SQUARE_SIZE/3), int(r*SQUARE_SIZE+ SQUARE_SIZE/3))) 
				else:
					pygame.draw.rect(screen, DARK_GREY, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
				pygame.draw.rect(screen, DARK_GREY, (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 7)

def play():
	

	pygame.init()
	b = Board()


	screen_size = (width, height)

	game_won = False
	

	while game_won == False:


		screen = pygame.display.set_mode(screen_size)
		b.show(screen)
	

		cero = b.buscar_cero()
		
		pygame.display.update()

		game_won = b.check_win()

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_DOWN:
					b.cero_abajo(cero)

				elif event.key == pygame.K_UP:
					b.cero_arriba(cero)

				elif event.key == pygame.K_LEFT:
					b.cero_izquierda(cero)

				elif event.key == pygame.K_RIGHT:
					b.cero_derecha(cero)

		game_won = b.check_win()

		if game_won:
 
			screen = pygame.display.set_mode(screen_size)
			b.show(screen)
			pygame.display.update()

			print("Has ganado!!!!")
			# Dibujar pantalla de ganador
			pass

		
play()

