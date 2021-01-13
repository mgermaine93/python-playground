# Entrypoint file to be used in development
from string_bits import string_bits
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
