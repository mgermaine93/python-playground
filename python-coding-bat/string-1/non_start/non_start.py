# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

def non_start(a, b):
    new_a = a[1:]
    new_b = b[1:]
    return new_a + new_b
