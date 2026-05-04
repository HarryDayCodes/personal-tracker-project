# Objects and Methods (8.1) ~~~~~~~~~~~~~~~~ 

name = "DIP"
author = "Seth Godin"
year = "2026"

tuple_example = (name, author, year)
dict_example = {"name": name, "author": author, "year": year}  # Just a tuple with keys
access_dict = dict_example["name"]
dict_example["name"] = "Jimmy Carr" # Dictionaries = mutable, but their key-values are immutable - changing a key value like this will still mean 'Seth Godin' is somewhere in memory

# DEFINITION: Method = function which operates on the specific object it is attached to, eg:

for value in dict_example.values():
    print(value)

# The above method "values" returns all values stored in the dictionary object "dict_example"

# MUTABILITY
# strings = immutable (create new str object, rather than updating exisiting)
# lists = mutable (can be updated w/o creating new object)

# Classes and Objects (8.2) ~~~~~~~~~~~~~~~

# Constructors create non-standard objects (i.e. ones other than strings, lists etc...) 
from fractions import Fraction # Fraction is a class to create new bespoke "Fraction" objects - This line is a special initialisation function called a 'Constructor'
# A CLASS IS A BLUEPRINT OF AN OBJECT, AND MAY HAVE BESPOKE DECLARATIONS
# eg.
fraction_example = Fraction(2,5)
print(fraction_example.numerator) # This would print out 2 - numerator is a variable, on the object fraction_example created using the Fraction Class
# METHOD VS. VARIABLE:
from datetime import date
my_date = date(2026,05,01)
weekday = my_date.isoweekday() # calling a method (notice the parentheses)
my_month = my_date.month # accessing a variable

# Definining Classes (8.3) ~~~~~~~~~~~~~~~~~
# - Note: Usually PascalCase

class NameOfClass:
    # Class Definition goes here
    pass # pass identifies the class as a skeleton

class BankAccount:
    
    # The constructor
    def __init__(self, balance: float, owner: str):
        self.balance = balance 
        self.owner = owner # self.owner = attribute of the object, owner = variable & parameter in constructor method __init__
    
peters_account = BankAccount(100, "Peter Python") # BankAccount object using BankAccount class
peters_account.balance+=100 # MUTABLE (this doesn't create a new object, it updates the attribute of the existing object)

# USING OBJECTS FORMED FROM CLASSES

# this function creates a new bank account object and returns it
def open_account(name: str):
    new_account =  BankAccount(0, name)
    return new_account

# this function adds the amount passed as an argument to the balance of the bank account also passed as an argument
def deposit_money_on_account(account: BankAccount, amount: int):
    account.balance += amount

# DEFININNG METHODS (PART 8.4) ~~~~~~~~~~~~~~~~~~~~~~

# Classes which ONLY contain data attr are not very diff from dictionaries.... but when we add METHODS:

class BankAccount:

    def __init__(self, account_number: str, owner: str, balance: float, annual_interest: float):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.annual_interest = annual_interest

    # This method adds the annual interest to the balance of the account
    def add_interest(self):
        self.balance += self.balance * self.annual_interest

peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)
peters_account.add_interest()
print(peters_account.balance)  # This will print out 1500 + the added interest of 1.5%

# METHODS ONLY ACT ON THE OBJECT THEY ARE CALLED ON, NOT THE CLASS

# ENCAPSULATION!!!!!  ---- we hitting some OOP concepts!
# Definition: Client = the section of code which creates an object & uses the service provided by its methods
# Definition: Encapsulation = Maintaining the internal integrity of the object and offering suitable methods to ensure this

# When the data contained in an object is used only through the methods it provides, the internal integrity of the object is guaranteed
# In practice this means that, for example, a BankAccount class offers methods to handle the balance attribute, so the balance is never accessed directly by the client.
# These methods can then verify that the balance is not allowed to go below zero, for instance.

# IMPORTANT - The parameter name self is only used when referring to the features of the object as an instance of the class.

# MORE CLASS EXAMPLES (PART 8.5) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

