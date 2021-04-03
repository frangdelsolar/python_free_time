from config import *

SISTEMAS = {
	0: {'Nombre': 'Cardíaco',
		'Color': RED,
		'Enfermedades': [['Hipertensión', 4],
						 ['Colesterol Alto', 5],
						 ], 
		},
	
	1: {'Nombre': 'Respiratorio', 
		'Color': VIOLET,
		'Enfermedades': [['Bronquitis', 7],
				         ['Cáncer de pulmón', 24],
				         ['Gripe', 5],
				         ]
		},

	2: {'Nombre': 'Digestivo',
		'Color': BROWN,
		'Enfermedades': [['Cirrosis', 14],
						 ['Estreñimiento', 4],
						 ['Infección por Salmonella', 5],
						 ['Gastroenteritis', 5],
						 ],
		},

	3: {'Nombre':'Nervioso',
		'Color': BLUE,
		'Enfermedades': [['Estrés', 4],
						 ['Parálisis', 22],
						 ['Ataques epilépticos', 16],
						 ],
		},

	4: {'Nombre':'Muscular',
		'Color': VIOLACEO,
		'Enfermedades': [['Deficiencia de potasio', 4],
						 ['Distrofia muscular', 13],
						 ],
		},

	5: {'Nombre':'Renal', 
		'Color': ROJIZO,
		'Enfermedades': [['Cálculos renales', 7],
						['Insuficiencia renal', 13],
						['Nefritis lúpica', 16],
						],
		},
	6: {'Nombre':'Esquelético',
		'Color': BLANCO,
		'Enfermedades': [['Osteoporosis', 20],
						['Raquitismo', 11],
						['Artritis', 4],
						]
		},

	7: {'Nombre': 'Inmune',
		'Color': AMARILLO,
		'Enfermedades': [['Insomnio', 8],
						['Fotosensibilidad', 8],
						['Asma', 7],
						],
		},
	}


class Sistema():
	def __init__(self, num, nombre, enfermedades, color):
		self.id = num
		self.nombre = nombre
		self.enfermedades = enfermedades
		self.velocidad_de_recuperacion = 0.0001
		self.puntaje = 100
		self.color = color

	def update(self):
		for e in self.enfermedades:
			if e.adquirida == True:
				self.puntaje += -0.0001

		self.puntaje += self.velocidad_de_recuperacion
		if self.puntaje < 0:
			self.puntaje = 0
		elif self.puntaje > 100:
			self.puntaje = 100

	
	def __str__(self):
		return ('{}. Puntaje: {}. Velocidad de recuperación: {}'.format(self.nombre, self.puntaje, self.velocidad_de_recuperacion))

