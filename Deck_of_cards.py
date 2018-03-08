from random import shuffle 

class Human(object):
	def __init__(self, name):
		self.name = name
		self.hand = []
	def draw(self, num, deck):
		self.deck = deck
		for i in range(0, num):
			var = self.deck.cards.pop()
			self.hand.append(var)
		return self
	def display(self):
		print self.name
		for i in range(0, len(self.hand)):
			print self.hand[i].value, self.hand[i].suit
		return self



class Card(object):
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

class Deck(object):
	def __init__(self):
		self.cards = []
		suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
		values = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
		for i in range(0,4):
			for j in range(0,13):
				card = Card(suits[i], values[j])
				self.cards.append(card)
	def display(self):
		for i in range(0,len(self.cards)):
			print self.cards[i].value, self.cards[i].suit
		return self
	
    def shuff(self):
		shuffle(self.cards)
		return self


deck1 = Deck()
human1 = Human("Jack")
human2 = Human("Ted")
deck1.shuff()
human1.draw(5,deck1).display()
print " "
human2.draw(5,deck1).display()
print "  "
# deck1.display()
