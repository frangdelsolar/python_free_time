from vector import *
from particle import *
from config import *
from firework import *
import pygame
import sys



def play():
	game_over = False

	pygame.init()

	contador = 0
	
	fireworks = []
	f1 = Firework()
	fireworks.append(f1)

	bg = pygame.image.load("img/aranas.jpg")
	bg = pygame.transform.scale(bg, (SCREEN_SIZE))
	while not game_over:

		screen = pygame.display.set_mode(SCREEN_SIZE)
		screen.fill((7, 26, 76, 100))

		
		for f in fireworks:	
			f.draw(screen)
			f.update()
			
			if f.exploded and len(f.particles) <= 0:
				ind = fireworks.index(f)
				fireworks.pop(ind)
	
		print(len(fireworks))
		pygame.display.update()

		contador += 1

		if contador % 10 == 0:
			fn = Firework()
			fireworks.append(fn)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				
				fn = Firework()
				fireworks.append(fn)




play()