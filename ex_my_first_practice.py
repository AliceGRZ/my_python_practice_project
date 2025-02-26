###### Variables types ######
my_first_int = 5
my_first_string = " Hello"
my_first_float = 4.55
my_first_boolean = True 

def addSpace():
    print("\n")

###### Formatting and Comparison Operators ######
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
print("hello_world[3:7] - Slice operation. Extracts a portion of the string based on the specified range of indices," +
      "\n(starts from index 3, ends before 7): " + f"{hello_world[3:7]}")
# Negative indices count from the end of the string. For example, hello_world[-1] is '!'.

addSpace()
print("hello_world[::-1] - The slicing operation in Python reverses the string hello_world: " + f"{hello_world[::-1]}")

addSpace()
print("hello_world.upper() - Make all letters UUPER CASE: " + hello_world.upper())

addSpace()
print("hello_world.lower() - Make all letters lower case: " + hello_world.lower())

addSpace()
print("hello_world.startswith('Hello') -\n \
      Verify if variable start with certain character - Does 'Hello world!' starts with 'Hello'?: " 
      + f"{hello_world.startswith('Hello')}")

addSpace()
print("hello_world.endswith('gibberish')-\n \
      Verify if variable ends with certain character - Does 'Hello world!' ends with 'gibberish'?: " 
      + f"{hello_world.endswith('gibberish')}")

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

##### Conditions #####
### Boolean operators:
## Using AND condition
addSpace()
if name == "Alicja" and age == 30:
    print("Your name is %s, and you are also %d years old." % (name, age))
else:
    print("You are not a person that you claim to be!")

## Using OR condition 
addSpace()
if name == "Ala" or name == "Alicja":
    print("Your name is correct")
else:
    print("You are not a person that you claim to be!")

### The "in" operator
addSpace()
item = "tomatoes"
if item in shopping_list:
    print("We are buying tomatoes today")

addSpace()
statement = False
another_statement = True

### The "is" operator
if statement is True:
    print("Buy tomatoes")
    pass
elif another_statement is False: # else if
    pass # The pass in each block doesn't contribute to the program's behavior. It just indicates that "nothing happens here."
else:
    print("No need to buy anything")

# Unlike the double equals operator "==", 
# the "is" operator does not match the values of the variables, but the instances themselves. For example:
addSpace()    
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

### The "not" logical operator 
# Using "not" before a boolean expression inverts it:
addSpace()    
print(not False) # Prints out True
print((not False) == (False)) # Prints out False 

# change this code
addSpace()   
print("Task - Change the variables in the first section, so that each if statement resolves as True:") 
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

###### Loops ######
addSpace()
# The "for" loop
print("Shopping items in the 'for loop' - iteration: ")
for item in shopping_list:
    print(item)
addSpace()

# For loops can iterate over a sequence of numbers using the "range" and "xrange" functions. 
# The difference between range and xrange is that the range function returns a new list with numbers of that 
# specified range, whereas xrange returns an iterator, which is more efficient. 
# (Python 3 uses the range function, which acts like xrange). Note that the range function is zero based.

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)
addSpace()
# Prints out 3,4,5
for x in range(3, 6):
    print(x)
addSpace()
# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
addSpace()

# Generates a list of numbers from 0 to 9
numbers = range(10)
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generates a range object (like an iterator)
numbers = range(10)
addSpace()
for num in numbers:
    print(num)  # Outputs numbers from 0 to 9, one at a time

### "while" loops
# While loops repeat as long as a certain boolean condition is met. For example:
# Prints out 0,1,2,3,4
addSpace()
count = 0
while count > -5:
    print(count)
    count -= 1  


addSpace()
count = 0
while count > -5:
    print(count)
    count = count - 1  # count -= 1 (same thing)


addSpace()
count = 0
while count < 5:
    print(count)
    count += 1  


addSpace()
count = 0
while count < 5:
    print(count)
    count = count + 1  # count += 1 (same thing)

### "break" and "continue" statements
# break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, 
# and return to the "for" or "while" statement. A few examples:

# Prints out 0,1,2,3,4
addSpace()
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
addSpace()
for x in range(10): # The for loop iterates over numbers from 0 to 9 (because range(10) generates numbers from 0 to 9).
    
    if x % 2 == 0:  # The condition if x % 2 == 0: checks whether x is even. 
                    # % (modulus operator) returns the remainder when dividing x by 2.
                    # If x % 2 == 0, it means x is divisible by 2, so it is even.
        continue    # If x is even, the continue statement is executed.
                    # continue skips the rest of the loop body and moves to the next iteration.
                    # This means print(x) will not be executed for even numbers.

    print(x)        # If x is odd, the if condition is false, so continue is skipped.
                    # The print(x) statement runs, displaying the odd number.

'''Usually modulo is used for checking if a number is even or odd:
If a number is even, dividing it by 2 will leave a remainder of 0.
If a number is odd, dividing it by 2 will leave a remainder of 1.'''

### Else clause
#  When the loop condition of "for" or "while" statement fails then code part in "else" is executed. 
# If a break statement is executed inside the for loop then the "else" part is skipped. 
# Note that the "else" part is executed even if there is a continue statement.
addSpace()
count=0
while(count<5):
    print(count)
    count +=1 # Arithmetic Shortcut of count = count + 1
else:
    print("count value reached %d" %(count))

'''
Operator Shortcuts
+	+=
-	-=
*	*=
/	/=
%	%= 
'''

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")


numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
    ]

# Loop through and print out all even numbers from the numbers list in the same order they are received. 
# Don't print any numbers that come after 237 in the sequence.
addSpace()
# your code goes here
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)

#### Functions ####

def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

# print(a simple greeting)
addSpace()
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
addSpace()
my_function_with_args("Alicja Python", "a great year!")

#### Dictionaries ####

books = {

    "Anna Karenina":"Leo Tolstoy",
    "Madame Bovary":"Gustave Flaubert",
    "War and Peace":"Leo Tolstoy",
    "Adventures of Huckleberry Finn":"Mark Twain"
}

books ["The Stories of Anton Chekhov"] =  "Anton Chekhov"
addSpace()
print(books)


def list_the_books():
    addSpace()
    print("Those are the books I read: ")
    for book_title, author in books.items():
        print(f"{book_title} by the author {author}")

list_the_books()

books.pop("Anna Karenina")
addSpace()
print(books)


