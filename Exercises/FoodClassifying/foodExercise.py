from random import choice
#food will be a random choice from these listed
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])

#if food is either apple or grape print fruit
if food == 'apple' or food == 'grape':
	print("fruit")
elif food == 'bacon' or food == 'steak':
	print("meat")
elif food == 'dirt' or food == 'worm':
	print('yuck')