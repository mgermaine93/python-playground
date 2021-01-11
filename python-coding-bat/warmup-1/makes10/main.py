# Entrypoint file to be used in development
from makes10 import makes10
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
