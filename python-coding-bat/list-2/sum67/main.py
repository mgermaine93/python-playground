# Entrypoint file to be used in development
from sum67 import sum67
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
