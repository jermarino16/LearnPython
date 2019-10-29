#import random module
from random import randint

#get a random number


user_guess = ""
#loop at least once
while user_guess != "n":
	random_number = randint(1, 10)
	you_guessed_it = False
	while not you_guessed_it:
		#get user to guess
		user_guess = int(input("Guess a number! "))
		#tell them if they are correct
		if (user_guess == random_number):
			print("Nice job")
			you_guessed_it = True
		#tell them if they are too low
		elif user_guess < random_number:
			print("Too low yo")
		else:
			print("Too high baby")

	#let them play again if they want
	user_guess = input("do you want to play again? type exit to stop")