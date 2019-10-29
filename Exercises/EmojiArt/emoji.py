#We will build an emoji tower
print("We are going to build an emoji tower!")
#user input for length
longest_row = input("How long do you want the tower? ")

if longest_row:
	longest_row = int(longest_row)

	num_times = 0
	num_emojis_forwards = 1
	num_emojis_backwards = longest_row - 1
	while num_times < longest_row * 2:
		#print the forward rows
		if num_times < longest_row:
			print("\U0001f600" * num_emojis_forwards)
			num_emojis_forwards += 1
		#print the rows backwards
		else:
			print("\U0001f600" * num_emojis_backwards)
			num_emojis_backwards -= 1
		#increment number of times
		num_times += 1

else:
	print("Type something yo")