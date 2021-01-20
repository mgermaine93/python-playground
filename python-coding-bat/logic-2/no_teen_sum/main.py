# Entrypoint file to be used in development
from no_teen_sum import no_teen_sum
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
