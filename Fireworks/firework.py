from config import *
from particle import *
class Firework:
	def __init__(self):
		self.part = Particle([random.randint(0, WIDTH), HEIGTH], True, 3)
		self.particles = []
		self.exploded = False

	def update(self):
		if not self.exploded:
			self.part.update(GRAVEDAD)

			if self.part.speed[1] >= 0:
				self.exploded = True
				self.explode()
				
		for p in self.particles:
			p.update(GRAVEDAD)
			# if p.pos[1] < 0:
			# 	self.particles.pop(self.particles.index(p))
			if p.size < 1:
				self.particles.pop(self.particles.index(p))
			# print(len(self.particles))

	def explode(self):
		if self.exploded:
			for i in range(100):
				p = Particle([self.part.pos[0], self.part.pos[1]], False, random.randint(4, 10))
				p.color = self.part.color
				self.particles.append(p)


	def draw(self, screen):
		if not self.exploded:
			self.part.draw(screen)
			
		for p in self.particles:
				p.draw(screen)