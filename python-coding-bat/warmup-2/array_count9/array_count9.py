# Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
    count = 0
    for number in nums:
        if number == 9:
            count += 1
    return count
