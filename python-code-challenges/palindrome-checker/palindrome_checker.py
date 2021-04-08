"""
Write a Python function to determine if a given string is a palindrome.
Input is the string to evaluate.
Output is a Boolean value.
Only consider letter (A-Z).
Ignore case.
"""


def palindrome_checker(word_or_phrase):

    letters_only = ""
    lowered_input = word_or_phrase.lower()

    # filter out the non-letter characters
    for character in lowered_input:
        if character.isalpha():
            letters_only = "".join([letters_only, character])

    # reverse the input
    backwards_input = letters_only[::-1]

    # check for palindrome
    if backwards_input == letters_only:
        return True
    return False


palindrome_checker("123r4245grwer56")
