# Entrypoint file to be used in development
from alarm_clock import alarm_clock
from unittest import main

# Runs unit tests automatically
main(module="test_module", exit=False)
