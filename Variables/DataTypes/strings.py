#strings can be created with "" or ''

string1 = "yo"

string2 = 'hi there'

print(string1)
print(string2)

#string concatenation
string5 = string1 + " " + string2
print(string5)

#whatever you use throughout the file be consistent

#you can use these to make strings with these quotes
string3 = 'you are "cool"'
string4 = "'Thanks'"

print(string3)
print(string4)

## we can use f-strings, formatted strings to print stuff as well
x = 10
print(f"The number is {x}")

## we can access string indeces like other programming lanagues 
answer = "yes"

print(answer)
print(answer[0])
print(answer[-2])