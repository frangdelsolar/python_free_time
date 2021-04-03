from config import *
import pygame

class Fuel():
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.color = (255, 255, 0)
		self.radius = SQUARESIZE//25
		# self.sound = pygame.mixer.Sound("sounds/pacman_chomp.wav")

	def draw(self, screen):
		pygame.draw.circle(screen, (self.color), (self.col*SQUARESIZE + SQUARESIZE//2, self.row* SQUARESIZE+ SQUARESIZE//2), self.radius)

	def eat_sound(self):
		pygame.mixer.Sound.play(self.sound)
		pygame.mixer.music.stop()

class Nitro():
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.color = (255, 0, 255)
		self.radius = SQUARESIZE//5
		# self.sound = pygame.mixer.Sound("sounds/pacman_eatfruit.wav")

	def draw(self, screen):
		pygame.draw.circle(screen, (self.color), (self.col*SQUARESIZE + SQUARESIZE//2, self.row* SQUARESIZE+ SQUARESIZE//2), self.radius)

	def eat_sound(self):
		pygame.mixer.Sound.play(self.sound)
		pygame.mixer.music.stop()
