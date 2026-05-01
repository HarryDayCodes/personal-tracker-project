# Objects and Methods ~~~~~~~~~~~~~~~~

name = "DIP"
author = "Seth Godin"
year = "2026"

tuple_example = (name, author, year)
dict_example = {"name": name, "author": author, "year": year}  # Just a tuple with keys
access_dict = dict_example["name"]
dict_example["name"] = "Jimmy Carr" # Dictionaries = mutable, but their keys are immutable - changing a key value like this will still mean 'Seth Godin' is somewhere in memory

# DEFINITION: Method = function which operates on the specific object it is attached to, eg:

for value in dict_example.values():
    print(value)

# The above method "values" returns all values stored in the dictionary object "dict_example"

# MUTABILITY
# strings = immutable (create new str object, rather than updating exisiting)
# lists = mutable (can be updated w/o creating new object)

# Classes! ~~~~~~~~~~~~~~~

# Constructors create non-standard objects (i.e. ones other than strings, lists etc...) 
from fractions import Fraction # Fraction is a class to create new bespoke "Fraction" objects - This line is a special initialisation function called a 'Constructor'
# A CLASS IS A BLUEPRINT OF AN OBJECT, AND MAY HAVE BESPOKE DECLARATIONS
# eg.
fraction_example = Fraction(2,5)
print(fraction_example.numerator) # This would print out 2 - numerator is a declaration, on the object fraction_example created using the Fraction Class
# METHOD VS. DECLARATION (A method is a specific type of function associated with an object or class, while a declaration is a statement that informs the compiler about an identifier's name and type without necessarily providing the implementation (body))