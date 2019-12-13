class Card:

	allowed_suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
	allowed_values = ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

	def __init__(self, value, suit):
		if suit in Card.allowed_suits and value in Card.allowed_values:
			self.suit = suit
			self.value = value
		else:
			raise ValueError("You didnt enter correct card values, try again")

	def __repr__(self):
		return f"{self.value} of {self.suit}"
