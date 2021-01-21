# Entrypoint file to be used in development
from end_other import end_other
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
