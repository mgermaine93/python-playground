# Entrypoint file to be used in development
from string_splosion import string_splosion
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
