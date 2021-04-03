from vector import *
from particle import *
from config import *
from firework import *
from bag import Bag
import pygame
import sys



def play():
	game_over = False

	pygame.init()

	contador = 1
	
	gotas = []
	for i in range(10):
		g = Gota()
		gotas.append(g)

	a = Agua()
	b = Bag()

	color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	
	while not game_over:

		screen = pygame.display.set_mode(SCREEN_SIZE)
		screen.fill((7, 26, 76, 100))
		# screen.fill(color)
		
		mousex, mousey = pygame.mouse.get_pos()
		b.update(mousex, mousey)
		b.draw(screen)
		
		for g in gotas:
			if (g.x >= mousex-int(b.size//2) and g.x<=mousex+int(b.size//2))  and (g.y >= mousey-int(b.size//2) and g.y<=mousey+int(b.size//2)):
				b.size+=g.length*0.01

				gotas.pop(gotas.index(g))

			elif (g.x >= mousex-b.size*2 and g.x<=mousex+b.size*2)  and (g.y >= mousey-b.size*2 and g.y<=mousey+b.size*2):
				if g.x > mousex:
					g.xspeed = random.randint(0,10) 
				else:
					g.xspeed = -random.randint(0,10)
				g.yspeed = -g.yspeed*0.7 
				g.zspeed = random.randint(0,10)*random.choice([-0.02, 0.02]) 
				g.color = (255, 255, 255)

			
			if g.splash:
				a.waterCount += 5
			g.update()
			g.draw(screen)

		# a.update()
		# a.draw(screen)



		pygame.display.update()

		contador += 1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
play()