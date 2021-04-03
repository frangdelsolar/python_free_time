import pygame
import random
import sys


clock = pygame.time.Clock()
scl = 10
width = 600
height = 400
GREY = (220, 220, 220)
GREEN = (11, 102, 35)
RED = (255, 105,0)
TURQUESA = (135, 206, 235)


class Ghost():

	def __init__(self):
		self.x = 64
		self.y = height // 2
		self.gravity = 0.35
		self.lift = -20
		self.velocity = 0
		self.points = 0 

	def update(self):
		self.velocity += self.gravity
		self.velocity *= 0.9
		self.y += self.velocity

		if self.y > height:
			self.y = height
			self.velocity = 0

		if self.y < 0:
			self.y = 0
			self.velocity = 0

		self.y = int(self.y//1)

	def show(self, screen):
		objectImg = pygame.image.load('ghost.png')
		objectImg = pygame.transform.scale(objectImg, (80, 80))
		# pygame.draw.circle(screen, RED, (self.x, self.y), scl)
		screen.blit(objectImg, (self.x,self.y))

	def up(self):
		self.velocity += self.lift

class Coin():
	def __init__(self):

		self.x = width
		self.y = random.randint(0, height)
		self.speed = 25
		self.highlight = False

	def show(self, screen):
		objectImg = pygame.image.load('coin.png')
		objectImg = pygame.transform.scale(objectImg, (40, 40))
		screen.blit(objectImg, (self.x,self.y))
		

	def update(self):
		self.x -= self.speed

	# def hits(self, bird):
	# 	if (bird.y < self.top) or (bird.y > (height-self.bottom)):
	# 		if (bird.x > self.x) and (bird.x <( self.x + self.w)):
	# 			self.highlight = True
	# 			return True

	# 	self.highlight = False
	# 	return False


def draw(screen_size, b, coins):
	screen = pygame.display.set_mode(screen_size)
	screen.fill(TURQUESA)

	for c in coins:
		c.show(screen)
		c.update()

		# if p.hits(b):
		# 	print("Ouch") 
		# 	return True


		# if p.x < (0-p.w):
			
		# 	b.points += 1
		# 	print(b.points)

		# 	i = pipes.index(p)
		# 	pipes.pop(i) 


	b.update()
	b.show(screen)
	
	pygame.display.update()

def is_over(bird, pipes):

	if bird.y == 0 or bird.y == height:
		return True


def play():

	pygame.init()
	screen_size = (width, height)
	
	game_over = False
	b = Ghost()
	coins = []
	coins.append(Coin())

	loop_count = 0

	pipe_collision = False

	while not game_over and not pipe_collision:
		
		tic = clock.tick(100000)

		if loop_count % 40 == 0:
			coins.append(Coin())

		# pipe_collision = draw(screen_size, b, pipes)

		draw(screen_size, b, coins)

		# game_over = is_over(b, pipes)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE:
					b.up()

		loop_count += 1


	
play()