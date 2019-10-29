#Loop through numbers 1 - 20

for x in range(1, 21):
	#if 4 or 13 print x is unlucky
	if x == 4 or x == 13:
		print(f"{x} is unlucky")
	#if even print x is even
	elif (x % 2) == 0:
		print(f"{x} is even")
	#else print x is odd
	else:
		print(f"{x} is odd")