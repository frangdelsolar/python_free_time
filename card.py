import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print ("{} de {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for value in range (1, 14):
            for suit in ["Corazones", "Diamantes", "Picas", "Tréboles"]:
                self.cards.append(Card(suit, value))

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

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self, index):
        return self.hand.pop(index)

fran = Player("Fran")
player2 = Player("Player2")
deck = Deck()

for i in range (7):
    fran.draw(deck)
    player2.draw(deck)


fran.showHand()
print()
value = int(input("valor: "))
fran.discard(value)
fran.showHand()
