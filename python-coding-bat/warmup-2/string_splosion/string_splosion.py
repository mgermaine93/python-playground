# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    new_string = ""
    for i in range(0, len(str) + 1):
        new_string += str[:i]
    return new_string
