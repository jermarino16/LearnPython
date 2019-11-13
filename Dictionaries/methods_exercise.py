inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

#copy inventory
stock_list = dict.copy(inventory)
print(f"The stock_list is : {stock_list}")

#add cookie to inventory
stock_list.update({"cookie": 18})
print(f"The stock_list is : {stock_list}")

#remove cake
stock_list.pop("cake")
print(f"The stock_list is : {stock_list}")