
#return highest value in a list
def max_magnitude(iterable):
    highest_num = 0
    for num in iterable:
        if abs(num) > highest_num:
            highest_num = abs(num)
    return highest_num


#simpler approach
def max_magnitude(nums):
    return max(abs(num) for num in nums)
