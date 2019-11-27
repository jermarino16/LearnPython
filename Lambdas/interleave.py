#interleaves 2 strings, "hi", "yo" would return hyio
def interleave(string1, string2):
       return ''.join(''.join(x) for x in (zip(str1,str2)))
