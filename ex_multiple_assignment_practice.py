from ex_my_first_practice import addSpace


many_variables = 3, 4 
addSpace()
print("wow, many_variables = 3, 4 - Assigment of many variables: " + f"{many_variables}")


# Handling Multiple Values at Once:
# Python supports multiple assignment and unpacking, which makes working with sequences concise.

x, y, z = 1, 2, 3  # Multiple assignment

a, b = 5, 10 # Swapping values without a temporary variable
a, b = b, a
print(a, b)  # Should print: 10 5
addSpace()
# Structuring Data:
# When dealing with collections (lists, tuples, dictionaries), assigning variables helps in accessing and organizing data.
person = {"name": "Alice", "age": 30}
name, age = person["name"], person["age"]
print(f"Person's name is {name} and is {age} years old")
addSpace()

# Basic Multiple Assignment
x, y, z = 1, 2, 3
print(x)  # 1
print(y)  # 2
print(z)  # 3
# Python unpacks the values on the right side (1, 2, 3) into the variables on the left (x, y, z).
addSpace()
# Unpacking Sequences (Lists, Tuples, Strings)
# You can unpack elements from a list, tuple, or even a string:
# Tuple unpacking
coordinates = (4, 7)
x, y = coordinates
print(x, y)  # 4 7
addSpace()
# String unpacking
a, b, c = "cat"
print(a, b, c)  # c a t
addSpace()


# Using the Asterisk (*) for Extended Unpacking
# The * operator lets you capture multiple values into a list:
numbers = [10, 20, 30, 40, 50]
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")
# Expected: First: 10, Middle: [20, 30, 40], Last: 50
#Handy when you need the first and last items but not the ones in between.
addSpace()

# Functions Returning Multiple Values
# Functions can return multiple values as a tuple, which can be unpacked directly:
def get_coordinates():
    return 10, 20  # Returns a tuple (10, 20)

x, y = get_coordinates()
print(f"x: {x}, y: {y}")  # x: 10, y: 20
addSpace()


# Python’s built-in divmod(a, b) returns a tuple with the quotient and remainder:
quotient, remainder = divmod(10, 3)
print(f"Quotient: {quotient}, Remainder: {remainder}")  # Quotient: 3, Remainder: 1
addSpace()


# Multiple Assignment in Loops
# Unpacking in for Loops
# When iterating over sequences of pairs (like lists of tuples), you can unpack values directly in the loop:
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

for number, letter in pairs:
    print(f"Number: {number}, Letter: {letter}")
addSpace()


# Using enumerate() with Multiple Assignment
# enumerate() returns pairs of (index, value), perfect for multiple assignment:
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
addSpace()

# Unpacking Dictionaries with .items()
# When iterating over a dictionary, items() returns (key, value) pairs:
person = {"name": "Alice", "age": 30}

for key, value in person.items():
    print(f"{key}: {value}")
addSpace()

# Nested Unpacking in Loops
# You can unpack nested structures if they’re consistent:
data = [("Alice", (25, "Engineer")), ("Bob", (30, "Designer"))]

for name, (age, profession) in data:
    print(f"{name} is a {age}-year-old {profession}.")
addSpace()

# Nested Unpacking
# You can unpack nested data structures like lists within tuples:
data = [("Tom", [80, 90, 85]), ("Jerry", [88, 92, 78])]

for name, (math, science, english) in data:
    print(f"{name} - Math: {math}, Science: {science}, English: {english}")
addSpace()

# Ignoring Values with _ (Underscore)
# When you don’t need certain values, use _ as a placeholder:
x, _, z = (10, 20, 30)
print(x, z)  # 10 30

data = [(1, 2, 3), (4, 5, 6)]

for _, y, _ in data:
    print(y)  # Only prints the middle value
addSpace()


# Iterate with Unpacking. For the dictionary below, print "John is 25 years old." and so on:
ages = {"John": 25, "Jane": 30, "Doe": 22}
for key, value in ages.items():
    print(f"{key} is {value} years old")
addSpace()

# Create a function calculate(a, b) that returns both the sum and product of two numbers. Unpack the results:
def calculate(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result
    
sum_result, product_result = calculate(4, 5)
print(f"Sum: {sum_result}, Product: {product_result}")  
addSpace()

# Challenge: Nested Data Unpacking
# Print each student's name and their math score:
students = [
    ("Alice", {"math": 90, "science": 85}),
    ("Bob", {"math": 78, "science": 92}),
]

for name, scores in students:
    print(f"{name} scored {scores['math']} in Math and {scores['science']} in Science")
addSpace()

for name, scores in students:
    for subject, score in scores.items():
        print(f"{name} scored {score} in {subject.capitalize()}")
addSpace()