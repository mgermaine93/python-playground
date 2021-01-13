# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
    count = 0
    # finding the shorter of the two prevents out-of-range errors
    if len(a) > len(b):
        shorter_string = a
    shorter_string = b
    # iterate through the first string
    for i in range(len(shorter_string) - 1):
        # compare one point of the first string with the same point in the second string
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count
