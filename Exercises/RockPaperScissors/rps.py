print("...rock...")
print("...paper...")
print("...scissors...")

#user input
print("Enter player 1's choice: ")
player1_choice = input()

#loop to print
count = 0
print("No cheating!")
while count < 80:
	print("NO CHEATING!")
	count += 1

print("Enter player 2's choice: ")
player2_choice = input()

#player1 wins set to false
player1_win = False
its_a_draw = False

#ensure use actually chose rock, paper or scissors

if (player1_choice == "rock" or player1_choice == "paper" or player1_choice == "scissors") and (player2_choice == "rock" or player2_choice == "paper" or player2_choice == "scissors"):
	##player 1 chooses rock
	if player1_choice == "rock":
		#player2 choices
		#rock is a draw
		if player2_choice == "rock":
			its_a_draw = True
		#scissors is a win	
		elif player2_choice == "scissors":
			player1_win = True

	##player 1 chooses paper
	elif player1_choice == "paper":
		#player 2 choices
		#paper is a draw
		if player2_choice == "paper":
			its_a_draw = True
		#rock is a win	
		elif player2_choice == "rock":
			player1_win = True

	##player 1  chooses scissors
	else:
		#player 2 choice
		#scissors is a draw
		if player2_choice == "scissors":
			its_a_draw = True
		#paper is a win for player 1
		elif player2_choice == "paper":
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
else:
	print("yo do you even know how to play")