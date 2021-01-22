# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.

def make_bricks(small, big, goal):
    remainder = goal % 5
    total = (big * 5) + small
    # Fail if not enough pieces, period
    if goal > total:
        return False
    # Fail if not enough small pieces to make up the difference
    if remainder > small:
        return False
    return True
