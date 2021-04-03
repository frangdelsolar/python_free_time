RECUPERACION = [['Nosocomefobia', 12],
				['Malos Médicos', 12],
				['Enfermeras en huelga', 12],
				['Placebo', 10],]


class Recuperacion():
	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.consecuencias = [] 
		self.precio = precio
		self.adquirido = False

	def __str__(self):
		return ('{}. Precio: {}. Adquirida: {}'.format(self.nombre, self.precio, self.adquirido))
