# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
    # python slice is [start:stop:step]
    # this says "return every other character of the string"
    return str[::2]
