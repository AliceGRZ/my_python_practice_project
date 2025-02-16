"""
Write a program that gets a dynamic number of input values.

The first input is a number that represents the number of the input values following it. 
The next input values are whole numbers.

In the end, print the sum of all the input numbers (not including the first input).
"""

n = int(input())
res = 0
for i in range(n):
    a = int(input())
    res += a
print(res)