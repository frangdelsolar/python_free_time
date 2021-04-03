import random
import copy
import pygame
import math
import sys

SQUARESIZE = 100

GREY = (220,220,220)
DARK_GREY = (169, 169, 169)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def draw_board(board, screen, size):

		
		# myfont.set_bold(True)

		for r in range(size):
			for c in range(size):
				pygame.draw.rect(screen, GREY, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE))
				
				
				

				if board[r][c] == 2:
					pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE))

				elif board[r][c] == 4:
					pygame.draw.rect(screen, GREEN, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE))



				if board[r][c] != 0:
					myfont = pygame.font.SysFont("roboto", 60)										
					
					if board[r][c] >= 10:
						myfont = pygame.font.SysFont("roboto", 50)

					elif board[r][c] >= 100:
						myfont = pygame.font.SysFont("roboto", 35)

					elif board[r][c] >= 1000:
						myfont = pygame.font.SysFont("roboto", 25)

					label = myfont.render(str(board[r][c]), 1, BLACK)
					screen.blit(label, (int(c*SQUARESIZE+SQUARESIZE/4), int(r*SQUARESIZE+ SQUARESIZE/4)))

				pygame.draw.rect(screen, DARK_GREY, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE), 5)


def check_availability(grid):
	list_availables = []

	for i in range(4):
		for j in range(4):
			if grid[i][j] == 0:
				list_availables.append((i, j))

	return list_availables


def get_number():
    if random.random() <= 0.9:
        return 2
    else:
        return 4


def randomize(grid):
	available_spots = check_availability(grid)
	r_spot = random.choice(available_spots)
	r_value = get_number()
	i, j = r_spot
	grid[i][j] = r_value
	return grid


def es_posible(juego, user_input):

	""" 
	El movimiento será posible si:
	- la copia del tablero es distinta del original antes del randomize
	"""

	copia = copy.deepcopy(juego) 
 
	decide(user_input, copia)
	sum(copia)
	slide(copia.grid)
	rotate_back(copia, user_input)	

	if copia.grid == juego.grid:
		return False
	return True


def ask_for_input(juego):
	user_input = input('Presioná w, s, a, d > ').lower()
	if ((user_input == "w") or (user_input == "s") or (user_input == "a") or (user_input == "d")) and es_posible(juego, user_input):
		return user_input
	ask_for_input(juego)


def buscar_not_zero(row):
	spot = 0
	for i in row:
		if row[i+1] == 0:
			pass
		else:
			spot = i


def sum(juego):
	grid = juego.grid
	for i in range(0, 4):
		# print('Estoy analizando esta fila', grid[i])
		for j in range(3):

			yo = grid [i][j]
			vecino = grid [i][j+1]

			if yo != 0:
				if vecino != 0:
					if yo == vecino:
						try:
							if yo != grid[i][j+2]:
								# print("Mi vecino y yo somos iguales. Nos sumaremos")
								grid[i][j+1] = yo + vecino
								grid[i][j] = 0
								juego.puntaje += grid[i][j+1]
								# print("Así queda la fila", grid[i])
								break
							else:
								# print("Somos tres iguales, debería dejarla pasar y que se las arregle el siguiente")
								pass
						except:
							# print("Mi vecino y yo somos iguales. Nos sumaremos")
							grid[i][j+1] = yo + vecino
							grid[i][j] = 0
							juego.puntaje += grid[i][j+1]
							# print("Así queda la fila", grid[i])
							break

					else:
						# print("Mi vecino y yo somos distintos, nos quedaremos en el molde", grid[i])
						pass

				else:
					try:
						otro_vecino = grid[i][j+2]
						if otro_vecino != 0:
							if yo == otro_vecino:
								try:
									if yo != grid[i][j+3]:
										# print("El otro vecino y yo somos iguales. Nos sumaremos")
										grid[i][j+2] = yo + otro_vecino
										grid[i][j] = 0
										juego.puntaje += grid[i][j+2]
										# print("Así queda la fila luego de la comparativa", grid[i])
										break
									else:
										# print("Somos tres iguales, debería dejarla pasar y que se las arregle el siguiente")
										pass	
								except:
									# print("El otro vecino y yo somos iguales. Nos sumaremos")
									grid[i][j+2] = yo + otro_vecino
									grid[i][j] = 0
									juego.puntaje += grid[i][j+2]
									# print("Así queda la fila luego de la comparativa", grid[i])
									break									

							else:
								# print("El otro vecino y yo somos distintos, nos quedaremos en el molde", grid[i])
								pass
						else:
							try:
								otro_vecino = grid[i][j+3]
								if otro_vecino != 0:
									if yo == otro_vecino:
										# print("El vecino de más allá y yo somos iguales. Nos sumaremos")
										grid[i][j+3] = yo + otro_vecino
										grid[i][j] = 0
										juego.puntaje += grid[i][j+3]
										# print("Así queda la fila luego de la comparativa", grid[i])
										break
									else:
										# print("El vecino de más allá y yo somos distintos, nos quedaremos en el molde", grid[i])
										pass
							except:
								# print("No hay nadie mucho más allá.")
								pass

					except:
						# print('No hay nadie al lado')
						pass
		# print("He terminado con esta fila.")

	juego.grid = grid

	return juego


def slide(grid):

	for i in range(0, 4):
		for j in range(3):
			if grid[i][j] != 0:
				if grid[i][j+1] == 0:
					grid[i][j+1] = grid[i][j]
					grid[i][j] = 0


def check_win(juego):
	for i in range(0, 4):
		for j in range(4):
			if juego.grid[i][j] == 2048:
				print("Has ganado!!! :D")
				juego.game_won = True


def rotate(juego):
	
	grid_rotado = [[0, 0, 0, 0],
				   [0, 0, 0, 0],
				   [0, 0, 0, 0],
				   [0, 0, 0, 0]]

	grid_rotado[0][3] = juego.grid[0][0]
	grid_rotado[1][3] = juego.grid[0][1]
	grid_rotado[2][3] = juego.grid[0][2]
	grid_rotado[3][3] = juego.grid[0][3]

	grid_rotado[0][2] = juego.grid[1][0]
	grid_rotado[1][2] = juego.grid[1][1]
	grid_rotado[2][2] = juego.grid[1][2]
	grid_rotado[3][2] = juego.grid[1][3]

	grid_rotado[0][1] = juego.grid[2][0]
	grid_rotado[1][1] = juego.grid[2][1]
	grid_rotado[2][1] = juego.grid[2][2]
	grid_rotado[3][1] = juego.grid[2][3]

	grid_rotado[0][0] = juego.grid[3][0]
	grid_rotado[1][0] = juego.grid[3][1]
	grid_rotado[2][0] = juego.grid[3][2]
	grid_rotado[3][0] = juego.grid[3][3]

	juego.grid = grid_rotado

	return juego


def decide(user_input, juego):
	if user_input == "d":
		return juego

	elif user_input == "w":
		rotate(juego)

	elif user_input == "a":
		rotate(juego)
		rotate(juego)

	elif user_input == "s":
		rotate(juego)
		rotate(juego)
		rotate(juego)


def rotate_back(juego, user_input):
	if user_input == "d":
		return juego

	elif user_input == "w":
		rotate(juego)
		rotate(juego)
		rotate(juego)


	elif user_input == "a":
		rotate(juego)
		rotate(juego)

	elif user_input == "s":
		rotate(juego)


class Jugar(object):
	def __init__(self):
		self.game_won = False
		self.puntaje = 0
		self.grid =[[0, 0, 0, 0],
					[0, 0, 0, 0],
					[0, 0, 0, 0],
					[0, 0, 0, 0]]
		self.play()

	def show(self):
		print("*************")
		print()
		for r in self.grid:
			print (r)
		print()
		print("*************")
		print("Puntaje", self.puntaje)
		print("*************")

	def play(self):
		print("Que comience el juego!")

		pygame.init()
		size = 4
		width = size * SQUARESIZE
		height = (size) * SQUARESIZE
		screen_size = (width, height)
		screen = pygame.display.set_mode(screen_size)
		
		draw_board(self.grid, screen, size)
		pygame.display.update()



		while self.game_won == False:
			

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()


				if event.type == pygame.KEYDOWN:
					print("Algo apretaste")

					if event.key == pygame.K_DOWN:
						user_input = 's'

					if event.key == pygame.K_UP:
						user_input = 'w'

					if event.key == pygame.K_LEFT:
						user_input = 'a'

					if event.key == pygame.K_RIGHT:
						user_input = 'd'


			

					try:
						randomize(self.grid)	
						draw_board(self.grid, screen, size)
						pygame.display.update()			

					except:
						print("No te quedan movimientos :'(")
						break
					
					self.show()
					




					# user_input = ask_for_input(self)
					decide(user_input, self)
					sum(self)
					slide(self.grid)
					rotate_back(self, user_input)
					check_win(self)
					
					draw_board(self.grid, screen, size)
					pygame.display.update()


juego = Jugar()
juego2 = Jugar()







