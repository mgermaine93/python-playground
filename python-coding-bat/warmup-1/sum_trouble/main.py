# Entrypoint file to be used in development
from sum_double import sum_double
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
