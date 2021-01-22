# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
    index = 0
    total = 0
    # Will break out once the index exceeds the length of the given list
    while index < len(nums):
        if nums[index] == 13:
            index += 2  # skip the value immediately after the 13
            continue  # and continue with the loop
        total += nums[index]
        index += 1  # avoids infinite loop
    return total
