# Entrypoint file to be used in development
from string_times import string_times
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
