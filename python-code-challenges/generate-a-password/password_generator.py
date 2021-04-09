"""
Write a Python function to generate pass-phrases.
The input should be an integer, representing the number of words in the pass-phrase.
The output should be a string of random words, separated by spaces.
"""
from words import words
import secrets


def password_generator(number_of_words):

    list_of_words = []

    if not isinstance(number_of_words, int):
        raise TypeError("Input must be an integer.")
    elif number_of_words > 5:
        raise ValueError(
            "Input must be an integer between 0 and five, inclusive.")
    else:
        for i in range(number_of_words):
            list_of_words.append(secrets.choice(words))

    print(" ".join(list_of_words))


password_generator("14")
