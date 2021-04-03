import pygame
import sys

from config import *
from vector import *
from projectile import Projectile
from brick import Brick


def play():
	
	pygame.init()
	pygame.display.set_caption('Bricks Breaker')

	clock = pygame.time.Clock()


	game_over = False
	game_won = False

	projectiles = []
	for i in range(10):
		projectiles.append(Projectile())

	bricks = []
	for r in range(5, 10):
		for c in range(size):
			bricks.append(Brick(r, c))
	
	while game_over == False and game_won==False:

		screen = pygame.display.set_mode(screen_size)
		
		for p in projectiles:
			p.update()
			p.draw(screen)

		for b in bricks:
			b.check_hit(projectiles)
			b.draw(screen)
			if b.points <= 0:
				bricks.pop(bricks.index(b))



		pygame.display.update()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:

				posx = event.pos[0]
				posy = event.pos[1]
				mouseclick = (posx, posy)		

				
				for p in projectiles:
					vm = Vector(p.coord(), mouseclick)
					xspeed, yspeed = vm.unit()
					p.xspeed = xspeed
					p.yspeed = yspeed
					p.xacc = 0
					p.yacc = 0

			
play()