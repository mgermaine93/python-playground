# Entrypoint file to be used in development
from string_match import string_match
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
