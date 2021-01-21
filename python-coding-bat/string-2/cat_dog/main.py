# Entrypoint file to be used in development
from cat_dog import cat_dog
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
