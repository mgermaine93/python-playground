# Entrypoint file to be used in development
from centered_average import centered_average
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
