import re
def is_valid_time(time):
	time_regex = re.compile(r'\d\d?:\d{2}')
	match = time_regex.fullmatch(time)
	if match:
		return True
	return False

# print(is_valid_time("10:45"))
# print(is_valid_time("1:23"))
# print(is_valid_time("10.45"))
# print(is_valid_time("1999"))
# print(is_valid_time("145:23"))

print(is_valid_time("it is 12:15"))
print(is_valid_time("12:15"))
print(is_valid_time("34:55"))
