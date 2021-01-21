# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

def end_other(a, b):
    lowercase_a = a.lower()
    lowercase_b = b.lower()
    if lowercase_a[-len(b):] == lowercase_b:
        return True
    elif lowercase_b[-len(a):] == lowercase_a:
        return True
    return False
