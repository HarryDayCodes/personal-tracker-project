# From "Python Object Oriented Programming (OOP) - Full Course for Beginners" - (https://www.youtube.com/watch?v=iLRZi0Gu8Go)
from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email # Showcases the instance attribute = "private" (e.g. it can't be used outside the class)
        self.password = password
    
    # This is a getter method (prefix w/ 'get' like below)
    def get_email(self):
        return self.__email  # This is used to get the private attribute outside of the class (why we use getter methods)
    
    # This is a setter method (prefix w/ 'set' like below)
    def set_email(self, new_email):
        print(f'Email accessed at {datetime.now()}') 
        self._email = new_email # Allows us to update 'private/protected' attributes
    
    # You could also validate email/username is of correct type when we make a setter

    def clean_email(self):
        return self.__email.lower().strip()
    

    
user1 = User("dantheman", "dan@gmail.com", "123") 

print(user1.get_email())
print(user1.set_email("dannewman@gmail.com"))
print(user1.clean_email())

# Protected (._) vs. private (.__) - protected > private unless ABSOLUTELY necessary to make private
# - both can be accessed w/in the class
# - protected can be accessed outside but we SHOULDN'T
# - privated CANNOT be accessed outside the class (these are a.k.a "Name Mangled")

# PROPERTY AND DECORATORS  INTRODUCTION ==========================================================

class PropUser:

    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property # getter decorator
    def email(self):
        print("Email Accessed")
        return self._email
    
    @email.setter # setter decorator - allows us to update email
    def email(self, new_email):
        if "@" in new_email:  # email validity checking
            self._email = new_email 

user2 = User("jennycoolidge", "4thofjuly@hotdog.com", "moistcookie")
user2.email = "This is not an email"  # Updating through setter properly
print(user2.email)


# STATIC ATTRIBUTES =====================================================
# - (aka class attribute)

class StaticUser:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email  # INSTANCE ATTRIBUTE
        StaticUser.user_count += 1  # STATIC ATTRIBUTE 

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")

user3 = StaticUser("dantheman", "dan@gmail.com") 
user4 = StaticUser("sally123", "sally@gmail.com")

print(StaticUser.user_count)
print(user3.user_count)
print(user4.user_count)

# Static Attributes = created ONCE at class level and shared between class it resides in and instance objects of that class
# Instance Attributes = created EVERY TIME we create a new instance (eg. user3, user4)

# STATIC METHODS ================
#   - Use @staticmethod decorator

class BankAccount:
    MIN_BALANCE = 100  # Constants = full caps by convention

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):  # Instance Method (as it needs access to instance attributes)
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance: £{self._balance}")
        else:
            print("Deposit amount must be positive.")

    @staticmethod # As it just exists to help the class, but DOESN'T need access to instance attributes
    def is_valid_interest_rate(rate):  # These are accessed from the class rather than instances of the class
        return 0 <= rate <= 5          # i.e. we use: BankAccount.is_valid_interest_rate, rather than account.is_valid_interest_rate
    

account = BankAccount("Alice", 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))

# ENCAPSULATION ===========================

# - Allows users to interact with an object w/o having to know about the internals of said object

class EncapBankAccount:

    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount >= self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

account = EncapBankAccount()
print(account.balance)
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
# print(account.balance)
# account.withdraw(1)

# ABSTRACTION ====================

# - Aim = reduce complexity by hiding unnecessary details

class EmailService:

    def _connect(self): # protected method - indicates they are just used internally by the class
        print("Connecting to email server...")

    def _authenticate(self): # Authenticate and connect are internal protected methods - no user will care about these
        print("Authenticating...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server...")

email = EmailService() # Instanciation!
email.send_email()

# INHERITENCE =================

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle): # Inheritence - note this!
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def start(self):  # Implementing it's own version of Vehicle's methods
        print("Car is starting.")

    def stop(self):
        print("Car is stopping.")   

class Bike(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

car = Car("Ford", "Focus", 2008, 5)
bike = Bike("Honda", "Scoopy", 2018)
print(car.__dict__) # prints class object as a dictionary

# POLYMORPHISM =====================

class Motorcycle(Vehicle): 
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def start(self):  # Implementing it's own version of Vehicle's methods
        print("Motorcycle is starting.")

    def stop(self):
        print("Motorcycle is stopping.")
    
vehicles: list[Vehicle] = [  # Vehicles = list of vehicle objects (This is known as type hinting)
    Car("Ford", "Focus", 2008, 5),
    Motorcycle("Honda", "Scoopy", 2018)
]

# Loop through list of vehicles and inspect them
for vehicle in vehicles: 
    vehicle.start() # These should change depending on if vehicle is car or motorcycle
    vehicle.stop()