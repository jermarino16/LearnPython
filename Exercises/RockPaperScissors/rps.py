#import random module
import random

print("...rock...")
print("...paper...")
print("...scissors...")

play_again = "y"
while play_again == "y":
	#user input for player 1
	print("Enter player 1's choice: ")
	player1_choice = input()

	#print buffer
	print("***NO CHEATING!***\n" * 80)

	#get a random choice for player 2
	random_number = random.randint(0, 2)
	if random_number == 0:
		player2_choice = "rock"
	elif random_number == 1:
		player2_choice = "paper"
	else:
		player2_choice = "scissors"
	#print computer choice	
	print(f"Player 2 has chosen {player2_choice}")

	#player1 wins set to false
	player1_win = False
	its_a_draw = False

	#ensure use actually chose rock, paper or scissors

	if (player1_choice == "rock" or player1_choice == "paper" or player1_choice == "scissors") and (player2_choice == "rock" or player2_choice == "paper" or player2_choice == "scissors"):
		#check for a draw
		if player1_choice == player2_choice:
			its_a_draw = True
		else:	
			##player 1 chooses rock
			if player1_choice == "rock":
				#player2 choices
				#scissors is a win	
				if player2_choice == "scissors":
					player1_win = True

			##player 1 chooses paper
			elif player1_choice == "paper":
				#player 2 choices
				#rock is a win	
				if player2_choice == "rock":
					player1_win = True

			##player 1  chooses scissors
			else:
				#player 2 choice
				#paper is a win for player 1
				if player2_choice == "paper":
					player1_win = True

		#evaluate if it's a draw or print out winners
		if not its_a_draw:
			print("SHOOT!")
			if player1_win:
				print("Player 1 Wins!")
			else:
				print("Player 2 Wins!")
		else:
			print("It's a draw!")
		play_again = input("Do you want to play again? (y/n): ")

	else:
		print("yo do you even know how to play")