def decrement_list(list_of_nums):
    decremented_list = map(lambda x: x - 1, list_of_nums) 

    return list(decremented_list)

print(decrement_list([1,2,3]))
    