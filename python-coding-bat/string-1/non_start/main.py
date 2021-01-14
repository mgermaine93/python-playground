# Entrypoint file to be used in development
from non_start import non_start
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
