"""
Write a Python "waiting game"
When the game is run, it should print a message requesting that the user wait a random amount of time, somewhere between 2 to 4 seconds.
When the player presses "Enter", a timer should begin.
The player's goal is to wait the specified number of seconds and then press enter again ("...Try to press enter again after 4 seconds have passed...").
Once "Enter" is typed a second time, the elapsed time should display, along with the difference in time between the actual time and the elapsed time.
"""

import random
from colorama import init, Fore, Back
import time
init()  # for Windows use cases


def waiting_game():

    number_of_seconds = random.randint(2, 4)

    print(f"**************** Welcome to the Waiting Game ****************\n\nSee how well you tell how much time has passed.\n")
    input("Press Enter/Return to start the stopwatch.\n")

    start_time = round(time.perf_counter(), 1)

    input(
        f"Press Enter/Return again when you think {number_of_seconds} seconds have passed.\n")

    elapsed_time = round(time.perf_counter(), 1) - start_time

    if elapsed_time == number_of_seconds:
        print(Fore.GREEN + "Wow, well done!  Nice timing!\n")
    if elapsed_time >= number_of_seconds:
        difference = round(elapsed_time - number_of_seconds, 1)
        print(Fore.RED + f"You were {difference} seconds too slow!\n")
    else:
        difference = round(number_of_seconds - elapsed_time, 1)
        print(Fore.RED + f"You were {difference} seconds too fast!\n")

    response = input(Fore.WHITE + "Play again? (y/n)\n")

    if response.lower() in ["y", "yes", "yeah", "sure"]:
        waiting_game()
    else:
        print("Thanks for playing!\n")


waiting_game()
