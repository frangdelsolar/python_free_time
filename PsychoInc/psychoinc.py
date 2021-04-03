from paciente import *
from player import *
from enfermedades import *


class PsychoInc():
	def __init__(self):
		self.player = None
		self.paciente = None
		self.build()

	def is_over(self):
		if self.player.dias_transcurridos == 100:
			return True
		return False

	def is_won(self):
		zero = []
		for s in self.paciente.sistemas:
			if s.puntaje < 1:
				zero.append(s)

		if len(zero) == len(self.paciente.sistemas):
			return True
		return False

	def build(self):
		self.player = Player()
		self.paciente = Paciente()


	def show(self):
		self.player.show()
		print()
		self.paciente.show()
		print()