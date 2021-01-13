# Entrypoint file to be used in development
from array123 import array123
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
