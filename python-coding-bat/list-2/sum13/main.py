# Entrypoint file to be used in development
from sum13 import sum13
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
