# Entrypoint file to be used in development
from reverse3 import reverse3
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
