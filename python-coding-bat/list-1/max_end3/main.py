# Entrypoint file to be used in development
from max_end3 import max_end3
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
