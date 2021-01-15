# Entrypoint file to be used in development
from sum3 import sum3
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
