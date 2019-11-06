#create some lists, and then make new lists using comprehensions


names = ["Elie", "Tim", "Matt"]
answer = [person[0] for person in names]
print(f"Our starting list is: {names} ")
print(f"The first letters of the list are: {answer} ")

numbers = [1,2,3,4,5,6]
evens = [val for val in numbers if val % 2 == 0]
print(f"Our number list is: {numbers} ")
print(f"The even numbers are: {evens} ")