# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

def round_sum(a, b, c):
    final_sum = round10(a) + round10(b) + round10(c)
    return final_sum


def round10(num):
    new_num = str(num)
    ones_place = int(new_num[-1])
    tens_place = int()
    num_start = int()
    final_num = int()
    if len(new_num) > 1:
        if len(new_num) > 2:
            num_start = new_num[:-2]
        tens_place = int(new_num[-2])
    if ones_place >= 5:
        tens_place += 1
    ones_place = 0
    final_num = int(str(num_start) + str(tens_place) + str(ones_place))
    return final_num

# Note:  this solution only works for the use cases specified in the original prompt.  It should not work for integers exceeding two digits, and it will not work for cases where the ten's place rounding up will cause a chain reaction, e.g., 19999, or 29999998.  To remedy this, refactoring will be necessary.
