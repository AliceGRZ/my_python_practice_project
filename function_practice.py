"""
Write a program that gets one input, a number. 
The input number indicates how many times to execute the below function. 

Create a function that calculates the sum of all of the numbers between 1 and 10000 (including) and prints it, 
name the function however you like.
"""

def sum_numbers():
    res = 0
    for i in range(1, 10001):
        res += i
    print(res)

n = int(input())
for i in range(n):
    sum_numbers()