#create dictionary
dictionary_test = {"cat": "cool", "dog": "cooler", "age": 24, "isAwesome": True }
print(f"The dictionary looks like: {dictionary_test}")

dictionary_test2 = dict(name = "jeremy", age=50)
print(f"The 2nd dictionary looks like: {dictionary_test2}")

#access dicitonary
name_Dictionary = dictionary_test2["name"]
print(f"The name of dictionary_test2 is: {name_Dictionary}")

#iterate over a dictionary
instructor = {"name": "Jeremy", "age": 25, "isCool": True}

print ("\nThe values of instrcutor are: ")
for value in instructor.values():
	print(value)

print ("\nThe keys of instrcutor are: ")
for keys in instructor.keys():
	print(keys)

print ("\nThe items of instrcutor are: ")
for key, value in instructor.items():
	print(f"The key is {key}, The value is {value})