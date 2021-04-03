class Enfermedad():
	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.precio = precio
		self.adquirida = False

	def __str__(self):
		return ('{}. Precio: {}. Adquirida: {}'.format(self.nombre, self.precio, self.adquirida))
