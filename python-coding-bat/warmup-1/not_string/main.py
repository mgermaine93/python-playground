# Entrypoint file to be used in development
from not_string import not_string
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
