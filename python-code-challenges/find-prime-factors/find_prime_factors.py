# Input an integer greater than or equal to zero.
# Return a list of all the integer's prime factors.

"""
- Since all numbers are divisible by 1, start with 2.
- As long as the "num" is less than the number passed in, check to see if number/num has no remainder.
- If there isn't a remainder, we've found a prime factor.  Add it to the list of factors to be returned, and redefine "num" to be the quotient of number/num.
- If there is a remainder, increment "num" by one and try again.
"""


def find_prime_factors(number):

    factors = []
    num = 2

    while(num <= number):
        if (number % num == 0):
            factors.append(num)
            number = number/num
        else:
            num += 1
    return factors
