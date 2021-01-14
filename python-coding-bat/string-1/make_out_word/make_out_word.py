# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

def make_out_word(out, word):
    # split the "out" string into two equal halves
    first_half = out[:len(out)//2]
    second_half = out[len(out)//2:]
    return f"{first_half}{word}{second_half}"
