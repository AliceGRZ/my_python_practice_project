"""Create a program that performs the following tasks using range():

Print all numbers between 50 to 100 that are divisible by 7
Print the first 10 even numbers starting from 20
Count backwards from 30 to 10, showing only numbers divisible by 3
Find the sum of all numbers from 0 to 100 that are divisible by 5"""

# Task 1: Numbers divisible by 7
print("Numbers divisible by 7 between 50-100:")

for num in range(50, 100):
    if num % 7 == 0:
        print(num, end=", ")

# Task 2: First 10 even numbers from 20
print("\nFirst 10 even numbers from 20:")

for num in range(20,39):
    if num % 2 == 0:
        print(num, end=", ")

# Task 3: Count backwards from 30 to 10, showing only numbers divisible by 3
print("\nCounting backwards, divisible by 3:")

for num in range(30, 10, -1):
    if num % 3 == 0:
        print(num, end=", ")

# Task 4: Sum of numbers divisible by 5
print("\nSum of numbers divisible by 5 (0-100):")
total = 0
for num in range(0,101):
    if num % 5 == 0:
           total += num  # Add to the total sum
print(total)


"""You are given a code which prints the numbers from 1 to 100 (including).

Your task is to add if and continue statements so that all 
numbers except multiples of 3 will be printed. In other words, skip printing any number that is divisible by 3.

For example, the output should include 
1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, and so on, but should skip 3, 6, 9, 12, 15, 18, etc."""

print("\nNumners that are not divisible by 3:\n ")
for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i)

# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
for num in range(30,81):
    if num % 4 == 0:
        print(num, end=", ")

print()  # new line
# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
for num in range (15, 32, 2):
    print(num, end=", ")
  
print()  # new line
# Task 3: Counting backwards, divisible by 5
print("\nCounting backwards, divisible by 5:")
for num in range(50,9,-1):
    if num % 5 == 0:
        print(num, end=", ")


print()  # new line
# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")
product = 1
for num in range(1,31):
    if num % 3 == 0:
        product *= num
print(product) 