'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''

def make_song(count=99, beverage=99):
    while count >= 0:
        if count == 0:
            yield f"No more {beverage}!"
        elif count == 1:
            yield f"Only 1 bottle of {beverage} left!"
        else:
            yield f"{count} bottles of {beverage} on the wall."
            count -= 1
    raise StopIteration
    
stance = make_song(3, "kombucha")

print(stance)