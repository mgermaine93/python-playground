# Entrypoint file to be used in development
from without_end import without_end
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
