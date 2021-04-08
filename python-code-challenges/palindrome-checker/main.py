# This entrypoint file to be used in development. Start by reading README.md
from palindrome_checker import palindrome_checker
from unittest import main


# Run unit tests automatically
main(module='test_module', exit=False)
