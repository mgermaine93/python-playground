# Entrypoint file to be used in development
from missing_char import missing_char
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
