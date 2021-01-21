# Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
    new_string = ""
    for letter in str:
        new_string += (2 * (letter))
    return new_string
