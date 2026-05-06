# From "Learn Python OOP in under 20 minutes" - (https://www.youtube.com/watch?v=rLyYb7BFgQI)

class Microwave: # Follows CamelCase
    
    # Note - you can change 'self' to ANY WORD (e.g. instance, then instance.brand etc..) - 'self' is just pythonic
    def __init__(self, brand: str, power_rating: str) -> None:  # This is a "Dunder" method (Stands for Double Underscore) - "-> None" means it returns nothing
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False # This doesn't need to be in the initialiser as it's instance attribute is already assigned a parameter

    def turn_on(self) -> None:
        if self.turned_on: # If microwave is already turned on
            print(f'Microwave ({self.brand}) is already turned on')
        else:
            self.turned_on = True
            print(f'Microwave ({self.brand}) has been turned on')

    def turn_off(self) -> None:
        if self.turned_on: # If microwave is already turned on
            self.turned_on = False
            print(f'Microwave ({self.brand}) has been turned off')
        else:
            print(f'Microwave ({self.brand}) is already turned off')

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f'Running ({self.brand}) for {seconds} seconds')
        else:
            print(f'A mystical force whispers: "Turn on your microwave first..."')

    # DUNDER METHOD! (a.k.a magic methods)
    def __add__(self, other) -> str:
        return f'{self.brand} + {other.brand}'
    
    # Useful dunder method -> str dunder method
    def __str__(self) -> str: # This gives us a legible string representation of our class
        return f'{self.brand}: {self.power_rating}' 


smeg: Microwave = Microwave("Smeg", "B")   # ": Microwave" = A type annotation, "Microwave()" is a constructor
bosch: Microwave = Microwave("Bosch", "C")   # ": Microwave" = A type annotation, "Microwave()" is a constructor
# print(smeg) # This gives a unique id pointing to "smeg", which is a unique instance of this Microwave
smeg.turn_on()
smeg.run(30)
smeg.turn_off()
smeg.run(10)
print(smeg + bosch) # uses the __add__ dunder method
print(smeg)  # This uses the __str__ dunder method that overrides the usually pointer it gives