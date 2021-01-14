# Entrypoint file to be used in development
from hello_name import hello_name
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
