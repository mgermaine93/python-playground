# Entrypoint file to be used in development
from first_half import first_half
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
