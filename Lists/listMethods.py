# Create a list called instructors
print("First let's create a liste")
instructors = ["jeremy"]
print(f"List is now: {instructors}")

#extend method, adds all of the info
print("\nNow lets use the extend method")
instructors.extend(["Colt", "Blue", "Lisa"])
print(f"List is now: {instructors}")

#we can also just append
print("\nWe can also just appened")
instructors.append(5)
print(f"List is now: {instructors}")

#or we can insert wherever
print("\nOr we can insert wherever into the list")
instructors.insert(1, "Cool cat")
print(f"List is now: {instructors}")

#we can pop items for the list, it takes the last item, and removes it but captures it at the same time
print("\nlet's pop something from the list")
removed_item = instructors.pop()
print(f"We are removing {removed_item}")
print(f"List is now: {instructors}")

#we can remove specific items in the list even if we dont know where it is
print("\n Let's remove \"Cool cat\" from the list")
instructors.remove("Cool cat")
print(f"List is now: {instructors}")

#we can also clear the list
print("\nLets clear the list with clear method")
instructors.clear()
print(f"List is now: {instructors}")
