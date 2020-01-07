def add_positive_numbers(x, y):
	assert x > 0 and y > 0, "Both must be positive"
	return x + y

print(add_positive_numbers(1,2))
print(add_positive_numbers(1,-2))