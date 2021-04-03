from config import *
from shooter import *
from spider import *
import pygame
import sys


def play():
	game_over = False

	pygame.init()

	sh = Shooter()

	bullets = []

	sps = []
	for i in range(10):
		sp = Spider()
		sps.append(sp)

		bg = pygame.image.load("img/aranas.jpg")
		bg = pygame.transform.scale(bg, (SCREEN_SIZE))



	while not game_over:
		screen = pygame.display.set_mode(SCREEN_SIZE)
		screen.fill((50,50,50))
		screen.blit(bg, (0,0))

		sh.draw(screen)
		for sp in sps:
			sp.draw(screen)
			sp.update()
		
		if len(bullets) > 0:
			for b in bullets:
				b.draw(screen)
				b.update()
				
				indb = bullets.index(b)
				if b.y <= 0:
					bullets.pop(indb)

			for b in bullets:
				indb = bullets.index(b)
				for sp in sps:					
					inds = sps.index(sp)
					
					if int(b.y) == int(sp.y):

						if (b.x >= int(sp.x - sp.size)) and (b.x <= int(sp.x + sp.size)) :
							bullets.pop(indb)
							sp.size += b.power
							if sp.size <= 6:
								sps.pop(inds)


		sh.update()
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_LEFT:
					sh.dir(-1, 0)
				if event.key == pygame.K_RIGHT:
					sh.dir(1, 0)
				if event.key == pygame.K_SPACE:
					b = sh.shoot()
					bullets.append(b)


play()