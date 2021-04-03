from psychoinc import *
from config import *
from virus import *
from graphics import *
import pygame
import sys
import math
import random



def debug_show(juego, contador, mouse):	
	juego.show()
	print('Contador', contador)
	print('Mouse', mouse)



def play():
	
	game_over = False
	game_won = False
	

	juego = PsychoInc()

	contador = 0
	frec_aparicion = 350

	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)
	screen.fill((255,255,255))
	bg = pygame.image.load("img/body.png")
	bg = pygame.transform.scale(bg, ((SQUARESIZE*8),SQUARESIZE*12))

	viruses = []

	while not game_over and not game_won:

		screen = pygame.display.set_mode(SCREEN_SIZE)
		screen.fill((230,230,230))

		contador += 1

		screen.blit(bg, ((SQUARESIZE*6)+random.randint(-1,0),0+random.randint(-1,0)))
		
		juego.player.draw(screen)
		juego.paciente.draw(screen)
		juego.paciente.update()
		


		if contador % 550 == 0:
			juego.player.dias_transcurridos += 1


		if contador % frec_aparicion == 0:
			sist = random.randint(0, 7)
			new_virus = Virus(sist)
			for r in juego.paciente.factores_de_riesgo:
				if r.adquirido == True:
					for a in r.afecciones:
						sa, se = a
						if sa == sist:
							new_virus.agresividad += new_virus.agresividad*se

			viruses.append(new_virus)
			frec_aparicion = random.randint(1, 400)

		for v in viruses:			
			v.draw(screen)			
			v.time -=1
			vi = viruses.index(v)
			if v.time == 0:
				viruses.pop(vi)
				
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				posy = event.pos[1]
				row = int(math.floor(posy/SQUARESIZE))

				mousepos = ((posx, posy), (row, col))

				for v in viruses:
					if  row == v.row and col == v.col:
						vi = viruses.index(v)
						viruses.pop(vi)
						juego.paciente.viruses.append(v)
						juego.player.puntos += 1

				if row == 11 and (col == 6 or col == 7):
				
					ver_ventas = True
					
					while ver_ventas:
						ver_ventas = draw_ventas(juego)

				debug_show(juego, contador, mousepos)
				
		if juego.is_won():
			print("Has ganado!!!!")
			game_won = True

		if juego.is_over():
			print('Has perdido!!! El paciente se ha recuperado...')
			game_over = True


play()