# Entrypoint file to be used in development
from parrot_trouble import parrot_trouble
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
