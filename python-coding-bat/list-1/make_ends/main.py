# Entrypoint file to be used in development
from make_ends import make_ends
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
