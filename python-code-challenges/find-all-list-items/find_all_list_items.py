"""
Write a Python function to index all items in a list that are equal to a given value.
It should accept to parameters:  the list to search, and the value to search for.
The output should be a list of indices, each represented by a list of numbers.
The function should be able to traverse multi-dimensional lists.
"""


def find_all_list_items(list_to_search, value_to_search_for):
    indices_of_values = []

    list_length = len(list_to_search)
    print(f"Length of the list: {list_length}")
    # ranges over the length of the provided list
    for i in range(len(list_to_search)):
        if list_to_search[i] == value_to_search_for:
            indices_of_values.append([i])
        elif isinstance(list_to_search[i], list):
            # use recursion to dig deeper into the nested lists
            # searches the sub-list found at index "i" above
            for index in find_all_list_items(list_to_search[i], value_to_search_for):
                # you'll get a list of indices that it finds
                indices_of_values.append([i]+index)

    return indices_of_values


find_all_list_items([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2)
