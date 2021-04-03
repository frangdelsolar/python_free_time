from config import *
import pygame

class Player():
	def __init__(self, name='SN'):
		self.name = name
		self.hand = []
		self.seleccion = None


	def show(self):
		print(self.name)
		for i in self.hand:
			print(i.letra, end=" ")
		print()


	def update_index(self):
		for i in range(len(self.hand)):
			self.hand[i].col = i

	def draw(self, screen):

		self.update_index()

		for f in self.hand:
			f.draw(screen)



		myfont = pygame.font.SysFont("roboto", 30)
		myfont.set_bold(True)

		turno_de = 'Es el turno de ' + self.name

		label = myfont.render(str(turno_de), 1, GREY)
		screen.blit(label, (int(SQUARESIZE/4), int(15*SQUARESIZE+ SQUARESIZE/4)))	
		
		
