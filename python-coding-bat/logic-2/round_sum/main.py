# Entrypoint file to be used in development
from round_sum import round_sum
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
