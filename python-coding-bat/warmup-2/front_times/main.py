# Entrypoint file to be used in development
from front_times import front_times
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
