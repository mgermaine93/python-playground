# Entrypoint file to be used in development
from make_bricks import make_bricks
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
