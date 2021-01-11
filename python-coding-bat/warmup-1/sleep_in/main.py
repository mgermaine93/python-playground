# Entrypoint file to be used in development
from sleep_in import sleep_in
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
