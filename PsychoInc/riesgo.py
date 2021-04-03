FACTORES_DE_RIESGO = [
					    {"Nombre": 'Hereditario',
					    'Precio': 7,
					    'Afecciones': [(0, 0.1), (4, 0.1), (6, 0.1)],
					    },

					    {"Nombre": '1',
					    'Precio': 0,
					    'Afecciones': [],
					    },

					    {"Nombre": '2',
					    'Precio': 0,
					    'Afecciones': [],
					    },

					    {"Nombre": 'Desnutrición',
					    'Precio': 5,
					    'Afecciones': [(2, 0.1), (5, 0.1), (6, 0.1)],
					    },

					    {"Nombre": 'Sobrepeso',
					    'Precio': 6,
					    'Afecciones': [(0, 0.1), (7, 0.1)],
					    },

					    {"Nombre": 'Obesidad',
					    'Precio': 10,
					    'Afecciones': [(0, 0.15), (2, 0.1), (4, 0.1)],
					    },

					    {"Nombre": 'Obesidad Mórbida',
					    'Precio': 14,
					    'Afecciones': [(0, 0.25), (1, 0.2), (4, 0.2)],
					    },

					    {"Nombre": 'Adicto a la comida chatarra',
					    'Precio': 9,
					    'Afecciones': [(2, 0.2), (5, 0.15)],
					    },

					    {"Nombre": 'Sedentario',
					    'Precio': 8,
					    'Afecciones': [(2, 0.2), (5, 0.15)],
					    },

					    {"Nombre": 'Mayor de 60',
					    'Precio': 12,
					    'Afecciones': [(0, 0.1), 
					    			 (2, 0.1),
					    			 (7, 0.1),
					    			 (4, 0.1),
					    			 (3, 0.1),
					    			 (5, 0.1),
					    			 (1, 0.1),
					    			 (6, 0.1),],
					    },

					    {"Nombre": 'Adicto al trabajo',
					    'Precio': 8,
					    'Afecciones': [(3, 0.2)],
					    },

					    {"Nombre": '3',
					    'Precio': 0,
					    'Afecciones': [],
					    },

					    {"Nombre": '4',
					    'Precio': 0,
					    'Afecciones': [],
					    },

					    {"Nombre": 'Desafortunado',
					    'Precio': 5,
					    'Afecciones': [],
					    },

					    {"Nombre": 'Fumador',
					    'Precio': 12,
					    'Afecciones': [(0, 0.1), (1, 0.25)],
					    },

					    {"Nombre": 'Alcohólico',
					    'Precio': 10,
					    'Afecciones': [],
					    },

					    {"Nombre": 'Deshidratación',
					    'Precio': 10,
					    'Afecciones': [],
					    },

					    {"Nombre": 'Alergias',
					    'Precio': 10,
					    'Afecciones': [],
					    },
					  ]


class FactorDeRiesgo():
	def __init__(self, nombre, precio, afecciones):
		self.nombre = nombre
		self.afecciones = afecciones
		self.precio = precio
		self.adquirido = False
	
	def __str__(self):
		return ('{}. Precio: {}. Adquirida: {}'.format(self.nombre, self.precio, self.adquirido))
