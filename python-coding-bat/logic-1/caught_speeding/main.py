# Entrypoint file to be used in development
from caught_speeding import caught_speeding
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
