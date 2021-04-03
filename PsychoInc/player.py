from config import *
import pygame 
import sys


class Player():
	def __init__(self):
		self.puntos = 0
		self.dias_transcurridos = 0
		self.recuperacion = 0

	def show(self):

		print("JUGADOR: ")
		print()
		print("Psycho Points: ", self.puntos)
		print("Dias transcurridos: ", self.dias_transcurridos)
		print("Recuperación: ", self.recuperacion)
		print()
		print()

	def draw(self, screen):

		pygame.draw.rect(screen, GREY, (SQUARESIZE*5, (SCREEN_SIZE[1]-SQUARESIZE), SQUARESIZE*10, SQUARESIZE))

		myfont = pygame.font.SysFont("roboto", SQUARESIZE)
		ppoints = myfont.render(str(self.puntos), 1, BLACK)
		dtrans = myfont.render(str(self.dias_transcurridos), 1, BLACK)
		recup = myfont.render(str(self.recuperacion), 1, BLACK)
		screen.blit(ppoints, (SQUARESIZE*6 +SQUARESIZE//2,(SCREEN_SIZE[1]-SQUARESIZE)+ SQUARESIZE//4))
		screen.blit(dtrans, (SQUARESIZE*9 +SQUARESIZE//2,(SCREEN_SIZE[1]-SQUARESIZE)+ SQUARESIZE//4 ))
		screen.blit(recup, (SQUARESIZE*12 +SQUARESIZE//2,(SCREEN_SIZE[1]-SQUARESIZE)+ SQUARESIZE//4 ))

