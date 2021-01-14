# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

def left2(str):
    first_two = str[0:2]
    ending = str[2:]
    return f"{ending}{first_two}"
