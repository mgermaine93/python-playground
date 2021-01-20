# Entrypoint file to be used in development
from lone_sum import lone_sum
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
