# Entrypoint file to be used in development
from same_first_last import same_first_last
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
