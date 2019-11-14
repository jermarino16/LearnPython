'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(num1, num2):
    if num1 > num2:
    	return "First is greater"
    elif num2 > num1:
    	return "Second is greater"
    else:
    	return "Numbers are equal"


print(number_compare(2, 1))
print(number_compare(1, 2))
print(number_compare(2, 2))
