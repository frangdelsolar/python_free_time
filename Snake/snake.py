import pygame

GREY = (220,220,220)
RED = (255,0,0)
scl = 20
width = 600
height = 600

clock = pygame.time.Clock()
tic = clock.tick(0.1)


def constrain(pos, inicio, fin):
	if pos <= inicio:
		return inicio

	elif pos >= fin:
		return (fin-scl)

	return pos


class Snake():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.xspeed = 1
		self.yspeed = 0
		self.total = 0
		self.tail = []


	def dir(self, x, y):
		self.xspeed = x
		self.yspeed = y

	def update(self, screen):
		
		for i in range(self.total):
			self.tail.append((self.x, self.y))

		self.x += self.xspeed * scl
		self.x = constrain(self.x, 0, width)
		self.y += self.yspeed * scl
		self.y = constrain(self.y, 0, height)
		
		print(self.tail)


	def show(self, screen):
		for i in self.tail:
			x, y = i
			pygame.draw.rect(screen, RED, (x, y, scl, scl))
			x += scl
			y += scl

		pygame.draw.rect(screen, GREY, (self.x, self.y, scl, scl))