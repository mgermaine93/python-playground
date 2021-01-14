# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty(length 0).

def combo_string(a, b):
    shorter_string = min([a, b], key=len)
    longer_string = max([a, b], key=len)
    return f"{shorter_string}{longer_string}{shorter_string}"
