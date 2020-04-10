# Import pyfiglet
from pyfiglet import figlet_format
# Import the colored module from the termcolor package
from termcolor import colored

# Store the available colors in a lighter-weight tuple rather than a list
valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

def print_art(message, color):
    # Sets the default color to cyan if the user inputs a color not listed above
    if color not in valid_colors:
        color = "cyan"

    # This is where the magic happens...
    ascii_art = figlet_format(message)

    # Pass the arguments to satisfy the colored module
    colored_ascii = colored(ascii_art, color=color)

    # This prints out the converted message to the command line
    print(colored_ascii)

# These messages print out to the command line when the program is run
message = input("What would you like to print? ")
color = input("What color would you like the message to be printed in? ")
print_art(message, color)