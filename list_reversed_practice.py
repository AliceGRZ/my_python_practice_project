"""
Write a function named reverse which gets a list of numbers as argument and returns the reversed list.
For example, for [1, 2, 3], the expected output is [3, 2, 1].
Don't use the reverse list 
"""


def reverse_1(lst):
    # Write code here
    reverse_list = []  # Create an empty list
    n = len(lst)  # Get the correct length of the input list
    
    for i in range(n - 1, -1, -1):  # Loop from last index to first
        reverse_list.append(lst[i])  # Append elements in reverse order
    
    return print(reverse_list)

def reverse_2(lst):
    res = []
    for i in range(len(lst)):
        res.append(lst[len(lst) - i - 1])
    return print(res)

list = [1,2,3,4,5,6,7,8,9,10]

reverse_1(list)
reverse_2(list)
