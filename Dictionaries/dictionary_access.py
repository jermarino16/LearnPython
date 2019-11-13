# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["almond croissant", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
quantity = bakery_stock.get(food)
if quantity:
	if quantity == 1:
		print(f"There is {quantity} {food} left")
	else:
		print(f"There are {quantity} {food}'s left")
else:
	print("we don't make that")