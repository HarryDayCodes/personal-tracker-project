# ==============================
# 🐍 PYTHON CHEAT SHEET (CORE)
# ==============================

# -------- VARIABLES ----------
x = 10            # int
y = 3.14          # float
name = "Alex"     # string
is_on = True      # boolean
nothing = None    # NoneType

# -------- DATA STRUCTURES ----------
# List (ordered, mutable)
nums = [1, 2, 3]
nums.append(4)
nums.remove(2)

# Tuple (ordered, immutable)
coords = (10, 20)

# Set (unordered, unique values)
unique_nums = {1, 2, 3}
unique_nums.add(4)

# Dictionary (key-value pairs)
person = {"name": "Alex", "age": 16}
person["age"] = 17

# -------- OPERATORS ----------
a, b = 5, 2
a + b   # addition
a - b   # subtraction
a * b   # multiplication
a / b   # division
a // b  # floor division
a % b   # modulus
a ** b  # exponent

# -------- COMPARISON ----------
a == b
a != b
a > b
a < b
a >= b
a <= b

# -------- LOGICAL ----------
True and False
True or False
not True

# -------- CONTROL FLOW ----------
if a > b:
    print("a bigger")
elif a == b:
    print("equal")
else:
    print("b bigger")

# Loops
for n in nums:
    print(n)

i = 0
while i < 3:
    i += 1

# -------- FUNCTIONS ----------
def add(x, y):
    return x + y

# Lambda (anonymous function)
square = lambda x: x * x

# -------- BUILT-IN FUNCTIONS ----------
len(nums)
type(x)
range(5)
sum(nums)
max(nums)
min(nums)

# -------- STRING METHODS ----------
text = "hello"
text.upper()
text.lower()
text.strip()
text.replace("h", "H")
text.split("e")

# -------- LIST METHODS ----------
nums = [1, 2, 3]
nums.append(4)
nums.pop()
nums.sort()
nums.reverse()

# -------- DICTIONARY METHODS ----------
person.keys()
person.values()
person.items()
person.get("name")

# -------- SET METHODS ----------
s = {1, 2, 3}
s.add(4)
s.remove(2)
s.union({5, 6})
s.intersection({1, 5})

# -------- EXCEPTIONS ----------
try:
    x = int("abc")
except ValueError:
    print("Error!")
finally:
    print("Done")

# -------- FILE HANDLING ----------
with open("file.txt", "r") as f:
    content = f.read()

# -------- CLASSES & OBJECTS ----------
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"

p = Person("Alex")
p.greet()

# -------- INHERITANCE ----------
class Student(Person):
    def study(self):
        return "Studying"

# -------- MODULES ----------
import math
math.sqrt(16)

# -------- LIST COMPREHENSION ----------
squares = [x**2 for x in range(5)]

# -------- COMMON CONCEPTS ----------
# Mutable: list, dict, set
# Immutable: int, float, string, tuple
# Indexing:
nums[0]
text[1]

# Slicing:
nums[0:2]
text[:3]

# ==============================
# END CHEAT SHEET
# ==============================