# Entrypoint file to be used in development
from has23 import has23
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
