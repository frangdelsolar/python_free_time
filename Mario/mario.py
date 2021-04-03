import pygame

class Mario():

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
		birdImg = pygame.image.load('bird.png')
		birdImg = pygame.transform.scale(birdImg, (60, 60))
		# pygame.draw.circle(screen, RED, (self.x, self.y), scl)
		screen.blit(birdImg, (self.x,self.y))

	def up(self):
		self.velocity += self.lift