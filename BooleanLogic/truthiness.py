animal = input("enter your favorite anmial\n")

#if the string is not empty then it prints something
if animal:
	print(animal + " is my favorite too")
else:
	print("you didnt say anything!")

#1 is always truthy, 0 is also falsy. none is also
if 1:
	print("Peace")
