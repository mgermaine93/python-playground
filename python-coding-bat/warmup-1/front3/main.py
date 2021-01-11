# Entrypoint file to be used in development
from front3 import front3
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
