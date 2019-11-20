def special_greeting(**kwargs):
	if "David" in kwargs and kwargs["David"] == "cool":
		return "You are cool David"
	elif "David" in kwargs:
		return "Hey David"

	return "Hey man You're not david"

print(special_greeting(David="cool"))
print(special_greeting(David="guy"))
print(special_greeting(Bob="guy"))