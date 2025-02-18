"""Write a function named prod which gets a list of numbers as argument and 
returns the product of all the numbers in the list.
Reminder, product is the multiplication of all the numbers, 
for [1, 2, 3], return 6 = 1 * 2 * 3."""

my_lst = [1, 2, 3, 4, 5, 6]

def prod(lst):
    total = 1
    for i in range(len(lst)):
        total *= lst[i]
    return print(total)





