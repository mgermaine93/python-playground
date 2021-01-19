# Entrypoint file to be used in development
from squirrel_play import squirrel_play
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
