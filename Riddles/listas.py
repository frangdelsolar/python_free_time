import random

	houses = [1, 2, 3, 4, 5]
	colors = ['Red', 'Green', 'White', 'Yellow', 'Blue'  ]
	nationalities = ['Brit', 'Swede', 'Dane', 'Norwegian', 'German' ]
	drinks = ['tea', 'coffee', 'milk',  'beer', 'water' ]
	smokes = ['Pall Mall', 'Dunhill', 'Blends', 'BlueMaster', 'Prince' ]
	pets = ['fish', 'dogs', 'birds', 'cats', 'horses', ]

class Solucion(Object):
	def __init__(self):
		self.house = random.choice(houses)
		self.color = random.choice(colors)
		self.nationality = random.choice(nationalities)
		self.drink = random.choice(drinks)
		self.smoke = random.choice(smokes)
		self.pet = random.choice(pets)

	def show(self):
		print()



			




