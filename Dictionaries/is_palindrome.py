#check back of the list by step of -1 to see if it's the same
def is_palindrome(string):
    return string == string[::-1]