# Entrypoint file to be used in development
from first_last6 import first_last6
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
