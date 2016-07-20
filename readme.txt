How to Run:
The main function setFinder.find_all_sets(board,n=3) itself does cannot be used outside of a larger program. To use it, it expects a dictionary of Card type objects with the key being the card id. An example of how to design this class is included in the setFinder module. The class must include a card id (cid) an dictionary of attributes. The card id can be of any object type, but works best as an integer. The n argument is the size of the Set. In normal play this is 3 but can be set to any other number. This function returns an iterator that runs through all valid Sets in the board.

The Card class can handle attributes of any type. However, the type must have a function for checking equivalence between two instances of the class. Importantly, if a new class is created, it is important that the equivalence function allows the class to work correctly during mathematical set operations such as unique.

An example of usage for both the Card class and the find_all_sets function can be found in the tests.py module. When run, this module runs the following four tests:
# test_1 - Each Attribute Changes, 4 card sets
# test_2 - 4 Cards, 3 card sets
# test_3 - No sets, 4 card sets
# test_4 - 3 card sets, 4 attribbutes each with 3 values
# test_5 - 3 card sets, 5 attributes, Flavor attribute has 6 values

Each test is set up in a csv file with a header line and then all the data rows. Each data row represents one card in the game. The first column must be the card id and the final colum must be a | (vertical bar) delimited list of all the sets that the card is a member of. The other columns in between are the attributes. Each attribute type must be unique, but can otherwise be any string. As it is currently set up, the data in the csv for a given attribute must also be a string. That is to say, it cannot be a reference to another location where the desired data is stored. In normal usage, any data type can be used, but currently for testing with csvs, it must be a string.

The module can be run from command line with no arguments as:
  python tests.py
Which will run all 5 aformentioned tests.
The user can also run with 2 arguments, a csv file of the game cards and the number of cards in the sets to be made, for example:
  python tests.py Tests/test_1.csv 4
  python tests.py Tests/test_2.csv 3
  python tests.py Tests/test_5.csv 4
