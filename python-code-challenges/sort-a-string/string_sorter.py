"""
Write a Python function to sort the words in a string.
Input should be a string of words, separated by spaces.
Return a string of words, sorted alphabetically.
Ignore the case of the words when sorting them.
Words in the output string should have the same case as the input words.
"""


def string_sorter(words):

    list_to_alphabetize = []
    list_of_words = words.split(" ")

    for word in list_of_words:

        # append a lowercase version of the word to the beginning of each word to make for easier sorting
        lowercase_word = word.lower()
        word_twins = lowercase_word + word

        # add the longer word to a new list
        list_to_alphabetize.append(word_twins)

    # sort the new list
    alphabetized_list = sorted(list_to_alphabetize)

    list_to_return = []

    for word in alphabetized_list:
        # remove the part of each word appended earlier
        original_word = word[(len(word)//2):]
        list_to_return.append(original_word)

    # remember to return a string, not a list
    string_to_return = " ".join(list_to_return)
    return string_to_return
