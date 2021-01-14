# Entrypoint file to be used in development
from first_two import first_two
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
