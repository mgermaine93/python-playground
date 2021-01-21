# Entrypoint file to be used in development
from count_code import count_code
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
