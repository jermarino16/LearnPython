#this program will simulate a bouncer

#ask for age
print("What is your age")
age = int(input())


#check for 21 +
if (age >= 21):
	print("Come in and party")
#check for 18 - 21
elif (age >= 18 and age < 21):
	print("Come in, but no drinks for you")
#check for < 18
else:
	print("You can't come in baby")