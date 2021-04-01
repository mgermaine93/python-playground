# This entrypoint file to be used in development. Start by reading README.md
from find_prime_factors import find_prime_factors
from unittest import main


# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
main(module='test_module', exit=False)
