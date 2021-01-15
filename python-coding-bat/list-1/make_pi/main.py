# Entrypoint file to be used in development
from make_pi import make_pi
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
