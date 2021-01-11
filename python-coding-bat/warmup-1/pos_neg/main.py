# Entrypoint file to be used in development
from pos_neg import pos_neg
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
