#use while loop to generate random number from 1 to 10 until you get 5
#incremt i each time
import random

i = 0
#loop until you get 5
while random_number != 5:
	random_number = random.randint(1, 10)
	i += 1

print (f"It took {i} tries to get the number 5")
