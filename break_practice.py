"""
Write a program that:

Takes two numbers as input
Creates a list of numbers from the first input to the second input (not including)
Finds and prints the first even number greater than 5
Then, in a separate loop, find and print the first number divisible by 7
"""


num1 = 1
num2 = 200

for num in range(num1, num2):
    if num > 5 and num % 2 == 0:
        print(f"First even number greater than 5: {num}")
        break

for num in range(num1, num2):
    if num % 7 == 0:
        print(f"First number divisible by 7: {num}")
        break
