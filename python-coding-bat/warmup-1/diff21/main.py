# Entrypoint file to be used in development
from diff21 import diff21
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
