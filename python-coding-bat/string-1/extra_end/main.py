# Entrypoint file to be used in development
from extra_end import extra_end
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
