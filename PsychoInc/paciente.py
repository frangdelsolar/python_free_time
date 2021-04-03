from enfermedades import *
from sistemas import *
from config import *
from riesgo import *
from recuperacion import *
import pygame
import random 


class Paciente():
	def __init__(self):
		self.sistemas = []
		self.velocidad_de_recuperacion = 0
		self.factores_de_riesgo = []
		self.recuperacion = []
		self.viruses = []
		self.build()


	def update(self):

		# actualizar los virus
		for v in self.viruses:
			v.update()
			if v.time == 0:
				vi = self.viruses.index(v)
				self.viruses.pop(vi)

		
		# actualizar los sistemas
		for s in self.sistemas:
			s.update()
			for v in self.viruses:
				if 	v.sistema == s.id:
					s.puntaje -= v.agresividad
					if s.puntaje < 0:
						s.puntaje = 0
							

	def build(self):

		for f in range(len(RECUPERACION)):
			nombre = RECUPERACION[f][0]
			precio = RECUPERACION[f][1]
			factor = Recuperacion(nombre, precio)
			self.recuperacion.append(factor)

		for f in range(len(FACTORES_DE_RIESGO)):
			nombre = FACTORES_DE_RIESGO[f]['Nombre']
			precio = FACTORES_DE_RIESGO[f]['Precio']
			afecciones = FACTORES_DE_RIESGO[f]['Afecciones']
			factor = FactorDeRiesgo(nombre, precio, afecciones)
			self.factores_de_riesgo.append(factor)	


		for i in range(3):
			f = random.choice(self.factores_de_riesgo)
			f.adquirido = True	
			for a in f.afecciones:
				pass
		print('Arreglá paciente.py 60')

		for i in range(len(SISTEMAS)):
			enfermedades = []
			for j in range(len(SISTEMAS[i]['Enfermedades'])):
				nombre = SISTEMAS[i]['Enfermedades'][j][0]
				precio = SISTEMAS[i]['Enfermedades'][j][1]
				enfermedad = Enfermedad(nombre, precio)
				enfermedades.append(enfermedad)
			sistema = Sistema(i, SISTEMAS[i]['Nombre'], enfermedades, SISTEMAS[i]['Color'])
			self.sistemas.append(sistema)


	def draw(self, screen):
		
		pygame.draw.rect(screen, GREY, (0, SQUARESIZE, SQUARESIZE*4, SQUARESIZE*10))
		myfont = pygame.font.SysFont("roboto", SQUARESIZE//2)

		r = 2
		for s in self.sistemas:
			leyenda = (s.nombre + ". " +  str(round(s.puntaje, 2)) + "%")
			mylabel = myfont.render(str(leyenda), 1, s.color)
			screen.blit(mylabel, (SQUARESIZE//2, r*SQUARESIZE))
			r+=1

	def draw_sistemas(self, screen):
		
		pygame.draw.rect(screen, GREY, (0, SQUARESIZE, SQUARESIZE*4, SQUARESIZE*10))
		myfont = pygame.font.SysFont("roboto", SQUARESIZE//2)

		r = 2
		for s in self.sistemas:
			leyenda = (s.nombre)
			mylabel = myfont.render(str(leyenda), 1, BLACK)
			screen.blit(mylabel, (SQUARESIZE//2, r*SQUARESIZE))
			r+=1


	def show(self):
		print("ESTADO GENERAL: ")
		print()

		for s in self.sistemas:
			print('SISTEMA', s.nombre)
			print('VELOCIDAD DE RECUPERACIÓN:', s.velocidad_de_recuperacion)
			print('PUNTAJE:', s.puntaje)
			print('ENFERMEDADES:')
			print()
			for e in s.enfermedades:
				if e.adquirida == True:
					print(e)
			print()		
			
		print("FACTORES DE RIESGO: ")
		print()
		for i in self.factores_de_riesgo:
			if i.adquirido == True:
				print(i)
		print()

		print("RECUPERACIÓN: ")
		print()
		for i in self.recuperacion:
			if i.adquirido == True:
				print(i)
		print()

		print("VIRUSES: ")
		print()
		for i in self.viruses:
			print(i, 'Agresividad:',  i.agresividad)
		print()