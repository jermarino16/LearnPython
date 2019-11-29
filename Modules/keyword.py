import keyword
#check to see if any strings are keywords, otherwise returns false
def contains_keyword(*args):
    for arg in args:
        if keyword.iskeyword(arg):
            return True

    return False