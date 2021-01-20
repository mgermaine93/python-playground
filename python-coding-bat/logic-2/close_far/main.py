# Entrypoint file to be used in development
from close_far import close_far
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
