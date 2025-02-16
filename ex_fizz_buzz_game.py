"""
Add a function named fizzbuzz that gets one number (int) as an argument, and:

If the number is divisible by 3, return "Fizz".
If the number is divisible by 7, return "Buzz".
If the number is divisible by both 3 and 7, return "FizzBuzz".
If none of the above conditions are met, return the number itself in a string format.
Finally print the output of the function
"""

print("Welcome to FizzBuzz!")

def fizzbuzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 7 == 0:
        result += "Buzz"
    if result == "":
        result = str(number)
    if result.count("3"):
        result = "Almost Fizz"
    return result

"""
Loop over the numbers from 1 to the number that the user entered, 
and each time use the function you created to calculate the 
FizzBuzz result and output it.
"""

limit = int(input())
# Play FizzBuzz
for i in range(1, limit + 1):
    print(fizzbuzz(i))


"""
Let's break down the solution code step by step:

print("Welcome to FizzBuzz!")
This line prints a welcome message to the user, indicating that the FizzBuzz program is starting.

def fizzbuzz(number):
Here, we define a function named fizzbuzz that takes one argument, number, which is expected to be an integer.

    result = ""
We initialize an empty string result. This will be used to build the output based on the conditions we check next.

    if number % 3 == 0:
        result += "Fizz"
This conditional checks if the number is divisible by 3 (i.e., the remainder when number is divided by 3 is 0). If it is, we append the string "Fizz" to result.

    if number % 7 == 0:
        result += "Buzz"
Similarly, this checks if the number is divisible by 7. If it is, we append "Buzz" to result.

    if result == "":
        result = str(number)
After checking both conditions, we check if result is still an empty string. If it is, that means the number was neither divisible by 3 nor by 7. In this case, we convert the number to a string and assign it to result.

    return result
Finally, we return the result, which will either be "Fizz", "Buzz", "FizzBuzz", or the string representation of the number itself.

limit = int(input())
This line prompts the user to input a number, which is then converted to an integer and stored in the variable limit.

print(fizzbuzz(limit))
Lastly, we call the `fizzbuzz
"""