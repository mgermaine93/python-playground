# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.

### STILL WORKING ON THIS ###

def make_bricks(small, big, goal):
    # False if not enough big
    # False if not enough small
    remainder = goal % 5
    # Divisible by 5
    if remainder == 0:
        if (big * 5) >= goal:
            return True
        elif (big * 5) + small >= goal:
            return True
        elif small >= goal:
            return True
    # Not divisible by 5
    elif (big * 5) + small >= goal:
        return True
    elif small >= goal:
        return True
    return False
