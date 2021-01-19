# Entrypoint file to be used in development
from sorta_sum import sorta_sum
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
