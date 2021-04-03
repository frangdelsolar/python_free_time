import random
import pygame

class Card(object):
    def __init__(self, suit, val, col, img):
        self.suit = suit
        self.value = val
        self.color = col
        self.col = 0
        self.row = 0
        self.shown = False
        self.placeholder = "*   *  *   *"
        self.img = img
        self.backImg = 'img/Back.png'

    def show(self):
        print ("{}, {}, ({})".format(self.value, self.suit, self.color))

    def draw(self, screen):

        if self.shown == True:
            objectImg = pygame.image.load(self.img)
        else: 
            objectImg = pygame.image.load(self.backImg)
        objectImg = pygame.transform.scale(objectImg, (15, 15))
        # pygame.draw.circle(screen, RED, (self.x, self.y), scl)
        screen.blit(objectImg, (100, 100))

    def __str__(self):
        if self.shown == True:
            return "{}, {}, ({}).".format(self.value, self.suit, self.color)
        else:
            return self.placeholder


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def __len__(self):
        return len(self.cards)

    def build(self):
        for value in range (1, 14):
            for suit in ["Cor", "Dia", "Pic", "Tre"]:
                if suit == 'Cor':
                    self.cards.append(Card(suit, value, 'R', 'img/corazon.png'))
                elif suit == 'Dia':
                    self.cards.append(Card(suit, value, 'R', 'img/diamante.png'))
                elif suit == 'Pic':
                    self.cards.append(Card(suit, value, 'N', 'img/picas.png'))
                elif suit == 'Tre':
                    self.cards.append(Card(suit, value, 'N', 'img/trebol.png'))



    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())

    def tomar_cartas(self, arr):
        self.hand.append(arr)

    def show_hand(self):
        print('En mano: ')
        for card in self.hand:
            card.show()

    def discard(self, index):
        return self.hand.pop(index)
