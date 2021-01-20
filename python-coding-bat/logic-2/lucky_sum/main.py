# Entrypoint file to be used in development
from lucky_sum import lucky_sum
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
