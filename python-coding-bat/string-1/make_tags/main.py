# Entrypoint file to be used in development
from make_tags import make_tags
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
