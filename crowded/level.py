from config import *
from board import *
from punto import Punto
import pygame
import sys
import math


class Level():
	
	def __init__(self):		
		self.board = Board(SIZE)
		self.puntos = []
		self.build()

	
	def build(self):
		for i in range(20):
			self.puntos.append(Punto())

		self.puntos[0].color = (0,255,0)
		self.puntos[0].equipo = 1

	def update(self):
		for p in self.puntos:
			try:
				if not p in self.board.grid[p.row][p.col].habitantes:
					self.board.grid[p.row][p.col].habitantes.append(p)
			except:
				pass

		for i in range(SIZE):
			for j in range(SIZE):
				self.board.grid[i][j].update()					

	def draw(self, screen):

		self.board.draw(screen)
		for p in self.puntos:
			p.update(self.board)
			p.draw(screen)
		






		


			

				
