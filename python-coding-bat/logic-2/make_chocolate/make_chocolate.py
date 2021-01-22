# We want make a package of goal kilos of chocolate. We have small bars(1 kilo each) and big bars(5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return - 1 if it can't be done.

def make_chocolate(small, big, goal):
    remainder = goal % 5
    big_weight = big * 5
    # If the big bars alone aren't enough, get the number of small bars needed
    if goal >= big_weight:
        remainder = goal - big_weight
    # If the small bars are enough, return the number needed
    if remainder <= small:
        return remainder
    # Otherwise, we don't have enough!
    return -1

# Times it can't be done:
# 1) When there's not enough pieces of chocolate, period
# 2) When there's not enough small pieces to make up the difference
