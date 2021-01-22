# Entrypoint file to be used in development
from make_chocolate import make_chocolate
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
