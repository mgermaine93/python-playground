# Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
    dog_count = 0
    cat_count = 0
    if len(str) > 2:
        for letter in range(len(str) - 2):
            if str[letter:letter + 3] == "cat":
                cat_count += 1
            if str[letter:letter + 3] == "dog":
                dog_count += 1
    if dog_count == cat_count:
        return True
    return False
