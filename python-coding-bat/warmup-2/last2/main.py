# Entrypoint file to be used in development
from last2 import last2
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
