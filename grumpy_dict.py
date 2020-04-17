# The class "GrumpyDict" inherits from "dict"
class GrumpyDict(dict):

    # Prints out the contents of the dictionary
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    # Tells you if something is not in the dictionary
    def __missing__(self, key):
        print("YOU WANT {key}?  WELL, IT AIN'T HERE!")

    # Sets a value in the dictionary
    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY?")
        print("OK, FINE...")
        super().__setitem__(key, value)

    # Another way to check to see if something is not in the dictionary
    def __contains__(self, item):
        print("SORRY, IT AIN'T HERE!")
        return False

# Don't have to define an __init__ because we're inheriting from dict and utilizing MRO
data = GrumpyDict({"first_name": "Edwin", "animal": "guinea pig"})
print(data)
data['habitat'] = 'grassy plains'
print(data)