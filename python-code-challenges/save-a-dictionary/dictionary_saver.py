"""
Write a Python function to save a dictionary object to a file.
The function should take two input arguments: the dictionary to save, and the output file path.
Write a second Python function to load the saved dictionary back into Python.
"""

import pickle


def dictionary_saver(dictionary_to_save, output_file_path):
    # save the dictionary
    # "wb" = "write binary"
    with open(output_file_path, "wb") as file:
        pickle.dump(dictionary_to_save, file)


def dictionary_loader(file_path):
    # "rb" = "read binary"
    with open(file_path, "rb") as file:
        return pickle.load(file)

# Test with different data types?
