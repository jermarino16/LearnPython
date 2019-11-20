def remove_negatives(list_of_nums):
    only_positives = filter(lambda x: x >= 0, list_of_nums)
    
    return list(only_positives)