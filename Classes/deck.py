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
		return f"The Deck has {len(self.cards)} cards"

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
	# def deal_card(self):
	# 	#returns a single card and uses deal method.

	# def deal_hand(self):
	# 	#accepts a number and uses the deal method to deal a list of cards
new_deck = Deck()

my_hand = new_deck.deal(5)
print(my_hand)
	