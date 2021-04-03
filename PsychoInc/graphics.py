from config import *
import pygame
import sys
import math
import random

def get_events():
	row, col = 0, 0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			
			posx = event.pos[0]
			col = int(math.floor(posx/SQUARESIZE))

			posy = event.pos[1]
			row = int(math.floor(posy/SQUARESIZE))

			mousepos = ((posx, posy), (row, col))
	return (row, col)


def draw_sist_venta(game, screen, index_sist):
	count = 1
	enfermedades = []
	for e in game.paciente.sistemas[index_sist].enfermedades:
		if e.adquirida == False:
			enfermedades.append(e)

	for e in enfermedades:
		e_row = SQUARESIZE * count
		pygame.draw.rect(screen, GREY, (SQUARESIZE*6, e_row, SQUARESIZE*6, SQUARESIZE*1))
		myfont = pygame.font.SysFont("roboto", 25)
		leyenda = e.nombre + '. ' + str(e.precio)
		mylabel = myfont.render(str(leyenda), 1, BLACK)
		screen.blit(mylabel, (SQUARESIZE*6 + SQUARESIZE//2, e_row + SQUARESIZE//2))
		count += 1
	
	pygame.display.update()
	row, col = get_events()

	for i in range(1, len(enfermedades)+1):
		if row == i and col>=6 and col <=12:
			if game.player.puntos >= enfermedades[i-1].precio:
				enfermedades[i-1].adquirida = True
				game.player.puntos -= enfermedades[i-1].precio
				screen = pygame.display.set_mode(SCREEN_SIZE)
				draw_ventas(game)
				draw_sist_venta(game, screen, i-1)
				pygame.display.update()

	for i in range(2, 10):
		if row == i and col>=0 and col <=5:
			index_sistema = i-2
			subs_venta = True
			screen = pygame.display.set_mode(SCREEN_SIZE)
			draw_ventas(game)
			while subs_venta:
				subs_venta = draw_sist_venta(game, screen, index_sistema)

	if row == 11 and (col == 6 or col == 7):
		return False
	
	return True


def draw_ventas(game):
	screen = pygame.display.set_mode(SCREEN_SIZE)
	game.paciente.draw_sistemas(screen)

	pygame.draw.rect(screen, GREY, (SQUARESIZE*6, (SCREEN_SIZE[1]-SQUARESIZE), SQUARESIZE*4, SQUARESIZE))
	myfont = pygame.font.SysFont("roboto", 25)
	mylabel = myfont.render(str('Volver'), 1, BLACK)
	screen.blit(mylabel, (SQUARESIZE*6 +SQUARESIZE//2,(SCREEN_SIZE[1]-SQUARESIZE)+ SQUARESIZE//4 ))
	
	
	myfont = pygame.font.SysFont("roboto", 40)
	ppoints = myfont.render(str(game.player.puntos), 1, BLACK)
	screen.blit(ppoints, (SQUARESIZE*8 +SQUARESIZE//2,(SCREEN_SIZE[1]-SQUARESIZE)+ SQUARESIZE//4 ))

	pygame.display.update()

	mouse_click = get_events()

	for i in range(2, 10):
		if mouse_click[0] == i and mouse_click[1]>=0 and mouse_click[1] <=5:
			index_sistema = i-2
			subs_venta = True
			while subs_venta:
				subs_venta = draw_sist_venta(game, screen, index_sistema)


	if mouse_click[0] == 11 and (mouse_click[1] == 6 or mouse_click[1] == 7):
		return False

	return True