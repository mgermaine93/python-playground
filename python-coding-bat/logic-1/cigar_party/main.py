# Entrypoint file to be used in development
from cigar_party import cigar_party
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
