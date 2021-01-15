# Entrypoint file to be used in development
from common_end import common_end
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
