# Entrypoint file to be used in development
from big_diff import big_diff
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
