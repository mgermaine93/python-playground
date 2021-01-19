# Entrypoint file to be used in development
from in1to10 import in1to10
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
