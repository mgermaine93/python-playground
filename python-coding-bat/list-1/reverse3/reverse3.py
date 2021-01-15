# Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

def reverse3(nums):
    # reverse() doesn't return a value, it just updates the existing list
    nums.reverse()
    return nums
