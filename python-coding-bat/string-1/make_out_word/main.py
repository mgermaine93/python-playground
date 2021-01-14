# Entrypoint file to be used in development
from make_out_word import make_out_word
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
