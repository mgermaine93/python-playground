# Entrypoint file to be used in development
from near_ten import near_ten
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
