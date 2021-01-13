# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
    count = 0
    if len(str) > 2:
        # this captures the last two characters of the provided string
        ending = str[-2:]
        # len(str) - 2 omits the ending, since the ending's not counted.
        for i in range(len(str) - 2):
            # compare the captured two characters to the ending
            if str[i:i+2] == ending:
                count += 1
    return count
