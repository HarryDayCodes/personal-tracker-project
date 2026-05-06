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
    def email(self, new_email)

user2 = User("jennycoolidge", "4thofjuly@hotdog.com", "moistcookie")
user2.email = "This is not an email"  # Updating through setter properly

