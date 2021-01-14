# Entrypoint file to be used in development
from left2 import left2
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
