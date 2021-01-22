# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

def sum67(nums):
    total = 0
    add_numbers = True
    for value in nums:
        if value == 6:
            add_numbers = False
        if add_numbers:
            total += value
        if value == 7:
            add_numbers = True
    return total
