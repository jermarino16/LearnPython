'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

def yes_or_no():
    yes = True
    
    while True:
        if yes:
            yield "yes"
            yes = False
        else:
            yield "no"
            yes = True
