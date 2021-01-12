# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) > 1:
        first_character = str[0]
        middle_characters = str[1:-1]
        last_character = str[len(str) - 1]
        return last_character + middle_characters + first_character
    else:
        return str
