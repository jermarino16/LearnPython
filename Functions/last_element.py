'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(list1):
    if list1:
        return list1[-1]
    return None


jer_list = ["Yo", 2, "Im the last"]
empty_list = []

print(last_element(jer_list))
print(last_element(empty_list))