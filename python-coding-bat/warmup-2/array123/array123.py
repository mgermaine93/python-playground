# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
    if len(nums) >= 3:
        # -2 prevents the iteration from going out-of-range
        for i in range(len(nums) - 2):
            if nums[i:i+3] == [1, 2, 3]:
                return True
    return False
