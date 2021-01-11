# Entrypoint file to be used in development
from front_back import front_back
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
