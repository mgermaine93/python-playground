# Entrypoint file to be used in development
from has22 import has22
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
