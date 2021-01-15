# Entrypoint file to be used in development
from middle_way import middle_way
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
