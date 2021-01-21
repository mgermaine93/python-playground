# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
    count = 0
    if len(str) > 3:
        for letter in range(len(str) - 3):
            if str[letter:letter + 2] == "co" and str[letter + 3] == "e":
                count += 1
    return count
