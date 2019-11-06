#create some lists, and then make new lists using comprehensions

#get first letters
names = ["Elie", "Tim", "Matt"]
answer = [person[0] for person in names]
print(f"Our starting list is: {names} ")
print(f"The first letters of the list are: {answer} ")

#even numbers
numbers = [1,2,3,4,5,6]
evens = [val for val in numbers if val % 2 == 0]
print(f"\nOur number list is: {numbers} ")
print(f"The even numbers are: {evens} ")

#intersect lists
numbers_1to4 = [1, 2, 3, 4]
numbers_3to6 = [3, 4, 5, 6]

intersection = [num for num in numbers_1to4 if num in numbers_3to6]
print(f"\nThe lists are: {numbers_1to4} and {numbers_3to6}")
print(f"The intersection is: {intersection}")

#reverse names and lowercase
#names = ["Elie", "Tim", "Matt"]
backwards_names = [(person[::-1].lower()) for person in names]
print(f"\nOur names list is: {names} ")
print(f"The backwards list is: {backwards_names} ")

#make a nested listed
nested_list = [[num for num in range(0,3)] for num1 in range (0,3)]
print(f"\nThe nested list is: {nested_list} ")