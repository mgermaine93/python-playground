# Entrypoint file to be used in development
from near_hundred import near_hundred
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
