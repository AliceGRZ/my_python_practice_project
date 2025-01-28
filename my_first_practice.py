###### Variables types ######
my_first_int = 5
my_first_string = " Hello"
my_first_float = 4.55
my_first_boolean = True 

def addSpace():
    print("\n")

###### Formatting and math symbols ######
addSpace()
print("Adding diffrent types of variables: " + f"{my_first_int + my_first_float}" + my_first_string + f" {my_first_boolean}")
addSpace()
print("Using symbol == (equal) to verify if 5 is equal to 4.55 - " + f"{my_first_int == my_first_float}")
addSpace()
print("Using symbol != (not equal) to verify if 5 is not equal to 4.55 - " + f"{my_first_int != my_first_float}")
addSpace()
print("Using symbol <= (smaller or equal) to verify if 4.55 is less or equal than 5 - " + f"{my_first_float <= my_first_int}")
addSpace()
print("Using symbol >= (grater or equal) to verify if 4.55 is greater or equal than 5 - " + f"{my_first_float >= my_first_int}")

wow, many_variables = 3, 4 
addSpace()
print("wow, many_variables = 3, 4 - Assigment of many variables: " + f"{wow , many_variables}")

# Multiplying strings to form a string with a repeating sequence
lots_of_hellos = "hello " * 10
addSpace()
print("Multiply string variable (hello * 10): " + lots_of_hellos)

###### Operators ######
number = 1 + 2 * 3 / 4.0
addSpace()
print("Equation (number = 1 + 2 * 3 / 4.0): " + f"{number}")

# Modulo operator calculates the part of the number that doesn't fit into full 
# divisors, i.e., the remainder of the division. For example: 7 % 3 = 1, 
# because 3 fits into 7 two times, and the remainder is 1.
modulo = 11 % 3
addSpace()
print("Modulo - What was left after fitting a number to another number (modulo = 11 % 3): " + f"{modulo}")

# Using two multiplication symbols makes a power relationship
squared = 7 ** 2
cubed = 2 ** 3
addSpace()
print("Power relationship (squared = 7 ** 2): " + f"{squared}")
print("Power relationship (squared = 2 ** 3): " + f"{cubed}")

# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
# together with a format string, which contains normal text together with 
# "argument specifiers", special symbols like "%s" and "%d".
# This prints out "Hello, John!"
name = "Alicja"
addSpace()
print("Using '%s %' operators to insert String variable: " + "Hello, %s!" % name)

# In Python's string formatting, the symbols %s and %d are used as format specifiers to 
# indicate the type of value you want to insert into a string:

# %s is used for strings. It tells Python to insert a string into the formatted text.
# Example: "Hello, %s!" % "world" would result in "Hello, world!".

# %d is used for integers. It tells Python to insert an integer into the formatted text.
# Example: "I have %d apples" % 5 would result in "I have 5 apples".

# %f: For floating-point numbers (decimals).

# Example: "The price is %f dollars" % 3.14 results in "The price is 3.140000 dollars".
# You can control the number of decimal places by using something like %.2f for 2 decimal places: "%.2f" % 3.14159 results in "3.14".
# %x: For hexadecimal (base 16) integers (lowercase).

# Example: "The number is %x" % 255 results in "The number is ff".
# %X: For hexadecimal integers (uppercase).

# Example: "The number is %X" % 255 results in "The number is FF".
# %o: For octal (base 8) integers.

# Example: "The number is %o" % 8 results in "The number is 10".
# %e: For scientific notation (e.g., 1.23e+04).

# Example: "The number is %e" % 123456 results in "The number is 1.234560e+05".
# %g: For floating-point numbers, uses either scientific notation or fixed-point notation, depending on the value.

# Example: "The number is %g" % 123456.789 results in "The number is 123456".
# %%: To insert a literal percent sign (%).

# Example: "Discount: 20%% off" results in "Discount: 20% off".

# Two or more argument specifiers, use a tuple (parentheses):
age = 25
addSpace()
print("Using '%s, %d %' operators to insert variable String and int: " + "%s is %d years old." % (name, age))

data = ("Alicja", "Python", 60.90)
format_string = "Hello %s %s. Your current balance is $%s."

addSpace()
print("Using '%' operators to insert a tuple (a fixed size list): " + format_string % data)

# Any object which is not a string can be formatted using the %s operator as well. 
# The string which returns from the "repr" method of that object is formatted as the string. For example:
# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
addSpace()
print("Using '%' operator to insert a list: " + "%s" % mylist)

addSpace()
hello_world = "Hello world!"
print("len(hello_world) - Verify how many characters are in word 'Hello world!' (including spaces): " + f"{len(hello_world)}")

addSpace()
print("hello_world.index('o') - Verify what index has certain character (Hello world! - letter 'o'): " + f"{hello_world.index('o')}")

addSpace()
print("hello_world.count('l') - Verify how many characters are in certain variable (Hello world! - letter 'l'): " + f"{hello_world.count('l')}")

addSpace()
print("hello_world[3:7] - Slice operation. Extracts a portion of the string based on the specified range of indices,\n(starts from index 3, ends before 7): " + f"{hello_world[3:7]}")
# Negative indices count from the end of the string. For example, hello_world[-1] is '!'.

addSpace()
print("hello_world[::-1] - The slicing operation in Python reverses the string hello_world: " + f"{hello_world[::-1]}")

addSpace()
print("hello_world.upper() - Make all letters UUPER CASE: " + hello_world.upper())

addSpace()
print("hello_world.lower() - Make all letters lower case: " + hello_world.lower())

addSpace()
print("hello_world.startswith('Hello') -\nVerify if variable start with certain character - Does 'Hello world!' starts with 'Hello'?: " + f"{hello_world.startswith('Hello')}")

addSpace()
print("hello_world.endswith('gibberish')-\nVerify if variable ends with certain character - Does 'Hello world!' ends with 'gibberish'?: " + f"{hello_world.endswith('gibberish')}")

addSpace()
split_the_word = hello_world.split(" ")
print("hello_world.split(" ") - Split the string 'Hello World!' into a list of substrings: " + f"{split_the_word}")

###### List features  ######
shopping_list = ["chesse", "milk", "bread", "chocolate", "butter", "coffee", "sample", "mint tea", "sample"]
item_number = [1,5,6,3,4]

# Joining Lists together
the_list = shopping_list + item_number
addSpace()
print("shopping_list + item_number - Adding two lists together: " + f"{the_list}")

# New lists with a repeating sequence using the multiplication operator:
addSpace()
print("[1,2,3] * 3 - Multiply list 3 times: " + f"{[1,2,3] * 3}")

# Counting the number of the same item on the list
sample_item = shopping_list.count("sample")
addSpace()
print("shopping_list.count('sample') - How many times certain variable is on the list - How many times there is 'sample'?: " + f"{sample_item}")

# Veryfing if item exists on the list
is_there_an_item = "coffee" in shopping_list
addSpace()
print("'coffee' in shopping_list - Is there certain variable on the list - Is there 'coffee?: " + f"{is_there_an_item}")

# Adding an item to a list
new_item = "wine"
shopping_list.append(new_item)
addSpace()
print("append(new_item) - Add new variable at the end of the list (append)- 'wine':\n" + f"{shopping_list}")

# Adding an item in certain place
shopping_list.insert(3, "tomatoes")
addSpace()
print("insert(3, 'tomatoes') - Add new variable in certain position - 'tomatoes - index 3:'\n " + f"{shopping_list}")

# Remove the last item
shopping_list.pop()
addSpace()
print("pop() - Remove the last variable form the list - 'wine' (oh no!):\n" + f"{shopping_list}")

# Remove certain item
shopping_list.remove("mint tea")
addSpace()
print("remove('mint tea') - Remove certain variable - mint tea:\n" + f"{shopping_list}")

# Verify the lenght of the list
items_taken = len(shopping_list)
addSpace()
def verifyIfWeCanShop(items_taken):
    addSpace()
    print("Method that checks if we have enough bags to make a shopping:")
    if items_taken > 10:
        print(f"{items_taken}" + " - Not enough bags")
    else: print(f"{items_taken}" + " - We can shop")

verifyIfWeCanShop(items_taken)

shopping_list.append("ham")
shopping_list.append("apple juice")

items_taken = len(shopping_list)
verifyIfWeCanShop(items_taken)

###### Loops ######
addSpace()
print("Shopping items in the 'for loop' - iteration: ")
for item in shopping_list:
    print(item)



