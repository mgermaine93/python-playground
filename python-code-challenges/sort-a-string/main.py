# This entrypoint file to be used in development. Start by reading README.md
from string_sorter import string_sorter
from unittest import main


# Run unit tests automatically
main(module='test_module', exit=False)
