# Create a list called instructors
print("First let's create a liste")
instructors = ["jeremy"]
print(instructors)

#extend method, adds all of the info
print("\nNow lets use the extend method")
instructors.extend(["Colt", "Blue", "Lisa"])
print(instructors)

#we can also just append
print("\nWe can also just appened")
instructors.append(5)
print(instructors)

#or we can insert wherever
print("\nOr we can insert wherever into the list")
instructors.insert(1, "Cool cat")
print(instructors)