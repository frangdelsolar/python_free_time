from Tablero import Board
from Fichas import Mazo
from Player import Player
from messages import *
from config import *
import pygame


class Scrabble():

	def __init__(self):
		self.board = None
		self.mazo = None
		self.players = []
		self.turno = None
		self.build()
		self.repartir()

	def build(self):
		def create_player():
			# name = ask_player_name()
			name = 'Pepe'
			player = Player(name)
			self.players.append(player)
		
		self.mazo = Mazo()
		self.board = Board()

		# players = ask_players()

		players = 1

		for i in range(players):
			create_player()

	def repartir(self):

		for j in range(len(self.players)):
			for col in range(7):
				ficha = self.mazo.fichas.pop(-1)
				ficha.row = 16
				ficha.col = col
				self.players[j].hand.append(ficha)
				


	def show_fichas(self):
		for f in self.mazo.fichas:
			f.show()

	def draw(self, screen, turno):
		
		turno.draw(screen)	
		self.board.draw(screen)

