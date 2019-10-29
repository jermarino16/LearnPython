#Loop through numbers 1 - 20

for x in range(1, 21):
	#if 4 or 13 print x is unlucky
	if x == 4 or x == 13:
		state = "unlucky"
	#if even print x is even
	elif (x % 2) == 0:
		state = "even"
	#else print x is odd
	else:
		state = "odd"
	print(f"{x} is {state}")