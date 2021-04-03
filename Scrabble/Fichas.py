from config import *
import random 
import pygame

class Ficha():
	def __init__(self, letra, puntaje):
		self.letra = letra
		self.puntaje = puntaje
		self.seleccionada = False
		self.row = None
		self.col = None
		self.x = None
		self.y = None


	def __str__(self):
		return (self.letra + str(self.row) + str(self.col))

	def draw(self, screen):

		myfont = pygame.font.SysFont("roboto", 30)
		myfont.set_bold(True)
		label = myfont.render(str(self.letra), 1, GREY)

		if not self.seleccionada:
			pygame.draw.rect(screen, (100,0,100), (self.col*SQUARESIZE,self.row*SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.rect(screen, (0,50,0), (self.col*SQUARESIZE,self.row*SQUARESIZE, SQUARESIZE, SQUARESIZE), 4)	
			screen.blit(label, (self.col*SQUARESIZE+SQUARESIZE//3, self.row*SQUARESIZE+SQUARESIZE//3))
		
		else:
			pygame.draw.rect(screen, (200,0,200), (self.x ,self.y, SQUARESIZE, SQUARESIZE))
			pygame.draw.rect(screen, (0,150,0), (self.x ,self.y, SQUARESIZE, SQUARESIZE), 4)
			screen.blit(label, (self.x+SQUARESIZE//3, self.y+SQUARESIZE//3))


	def update(self):
		pass

	def show(self):
		print("'{}', ({}). {}. {}".format(self.letra, self.puntaje, self.row, self.col))

class Mazo():
	def __init__(self):
		self.fichas = []
		self.build()
		self.shuffle()

	def build(self):
		for i in range(2):
			comodin = Ficha('@', 0)
			self.fichas.append(comodin)

		for i in range(12):
			A = Ficha('A', 1)
			self.fichas.append(A)
			
			E = Ficha('E', 1)
			self.fichas.append(E)

		for i in range(9):
			O = Ficha('O', 1)
			self.fichas.append(O)

		for i in range(6):
			I = Ficha('I', 1)
			self.fichas.append(I)

			S = Ficha('S', 1)
			self.fichas.append(S)

		for i in range(5):
			N = Ficha('N', 1)
			self.fichas.append(N)

			R = Ficha('R', 1)
			self.fichas.append(R)

			U = Ficha('U', 1)
			self.fichas.append(U)

			D = Ficha('D', 2)
			self.fichas.append(D)

		for i in range(4):
			L = Ficha('L', 1)
			self.fichas.append(L)		

			T = Ficha('T', 1)
			self.fichas.append(T)

			C = Ficha('C', 3)
			self.fichas.append(C)

		for i in range(2):
			G = Ficha('G', 2)
			self.fichas.append(G)

			B = Ficha('B', 3)
			self.fichas.append(B)

			M = Ficha('M', 3)
			self.fichas.append(M)

			P = Ficha('P', 3)
			self.fichas.append(P)

			H = Ficha('H', 4)
			self.fichas.append(H)

		F = Ficha('F', 4)
		self.fichas.append(F)

		V = Ficha('V', 4)
		self.fichas.append(V)

		Y = Ficha('Y', 4)
		self.fichas.append(Y)

		CH = Ficha('CH', 5)
		self.fichas.append(CH)

		Q = Ficha('Q', 5)
		self.fichas.append(Q)

		J = Ficha('J', 8)
		self.fichas.append(J)

		LL = Ficha('LL', 8)
		self.fichas.append(LL)

		letra = Ficha('Ñ', 8)
		self.fichas.append(letra)

		RR = Ficha('RR', 8)
		self.fichas.append(RR)

		X = Ficha('X', 8)
		self.fichas.append(X)

		Z = Ficha('Z', 10)
		self.fichas.append(Z)

	def shuffle(self):
	    for i in range(len(self.fichas) -1, 0, -1):
	        r = random.randint(0, i)
	        self.fichas[i], self.fichas[r] = self.fichas[r], self.fichas[i]
	
	def draw(self):
		pass

	def show(self):
		for i in self.fichas:
			i.show()
