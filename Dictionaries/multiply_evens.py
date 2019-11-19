'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(list_numbers):
    product = 1

    for x in list_numbers:
        if x % 2 == 0:
            product = product * x
        
    return product