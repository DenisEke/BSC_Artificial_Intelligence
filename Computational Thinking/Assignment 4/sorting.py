# My code for task 2 of assignment 4

# creating a class that represents a coordinate.
# I am sure that this isn't necessary but
# I don't really like python dicts and don't
# know python good enough to come up with an alternative
#
# NOTE: I found out that there a are tuples after I created this so I just left it as is
class Coord:

    # consturctor that takes the coors letter and number
    def __init__(self, letter, num):
        self.letter = letter
        self.num = num

    # it would be awesome to print the sorted array so this
    # function explains how to print this class
    def __repr__(self):
        return "(" + self.letter + ", " + str(self.num) + ")"


# A function that returns the letter value of a coord
def getLetter(coord):
    return coord.letter


# A function that returns the number value of a coord
def getNumber(coord):
    return coord.num


# array of the given coordinates
coords = [
    Coord("f", 9),
    Coord("z", 2),
    Coord("t", 4),
    Coord("x", 8),
    Coord("b", 1),
    Coord("m", 7),
]

# print unsorted array
print("Unsorted array: ", coords);

# sort array using my custom key function and print it
# this specifies a specific attribute by which to sort
coords.sort(key=getLetter)
print("Array sorted by letter: ", coords);

# same as above but with number
coords.sort(key=getNumber)
print("Array sorted by number: ", coords);
