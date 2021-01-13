# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

def array_front9(nums):
    for i in range(len(nums)):
        if i == 3:
            break
        if nums[i] == 9:
            return True
    return False
