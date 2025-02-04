"""

How It Works:
It takes an integer input n from the user.
Initializes a variable res = 1 to store the result.
Uses a for loop to multiply res by each number from 1 to n.
Finally, it prints the factorial of n.

Since 
5!=5*4*3*2*1=120

General Formula (Factorial)
n!=n*(n-1)*(n-2)*...*1
This code calculates n! for any positive integer 

"""


n = int(input())
res = 1

for i in range (1, n + 1):
    res *= i
print(res)