"""
Write a program that finds all pairs of numbers that add up to n using numbers from 1 to n - 1.
The program should show all possible combinations, including duplicate pairs in reverse order. 
For example, both "1 5" and "5 1" should be shown, as they are considered different arrangements of the same pair. 
Numbers can also be paired with themselves if their sum equals n.

For example if n = 6, the output should be:
"""

n = 8
# Write your code below
for i in range(1, n):
    for j in range(1, n):
        if i + j == n:
            print(i, j)

"""
Write a program that finds all pairs of numbers that multiply to give n using numbers from 1 to n.
The program should show all possible combinations, including duplicate pairs in reverse order. 
or example, both "1 6" and "6 1" should be shown, as they are considered different arrangements of the same pair. 
Numbers can also be paired with themselves if their product equals n.
"""
n = 9
# Write your code below
for i in range(1, n+1):
    for j in range(1, n+1):
        if i * j == n:
            print(i, j)