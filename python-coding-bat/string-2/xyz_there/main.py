# Entrypoint file to be used in development
from xyz_there import xyz_there
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
