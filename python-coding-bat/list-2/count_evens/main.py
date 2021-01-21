# Entrypoint file to be used in development
from count_evens import count_evens
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
