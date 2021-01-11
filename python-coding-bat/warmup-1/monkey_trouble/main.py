# Entrypoint file to be used in development
from monkey_trouble import monkey_trouble
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
