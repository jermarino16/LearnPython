from random import random

def flip_coin():
	#generate random number from 0 - 1
	if random() > 0.5:
		return "heads"
	else:
		return "tails"

print(flip_coin())