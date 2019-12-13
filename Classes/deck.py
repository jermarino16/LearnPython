import card
import random 


class Deck:

	def __init__(self):
		suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
		values = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
		self.cards = []
		for suit in suits:
			for value in values:
				self.cards.append(card.Card(value, suit))


	def __repr__(self):
	#return how many cards are in the deck
		return f"The Deck has {self.count()} cards"

	def count(self):
		return len(self.cards)

	def deal(self, num_to_deal):
		cards_to_deal = []
		if num_to_deal <= self.count():
			if num_to_deal == 1:
				return self.cards.pop(0)
			else:
				for x in range (0, num_to_deal):
					cards_to_deal.append(self.cards.pop(0))
				return cards_to_deal
		else:
			raise ValueError("You want to deal more than the deck has")

	def shuffle(self):
		random.shuffle(cards) 

	def deal_card(self):
		return self.deal(1)

	def deal_hand(self, num_to_deal):
		return self.deal(num_to_deal)
new_deck = Deck()

my_hand = new_deck.deal_card()
print(my_hand)
	