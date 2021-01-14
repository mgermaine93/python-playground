# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

def without_end(str):
    if len(str) > 2:
        return str[1:-1]
    else:
        return ""
