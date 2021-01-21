# Entrypoint file to be used in development
from count_hi import count_hi
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
