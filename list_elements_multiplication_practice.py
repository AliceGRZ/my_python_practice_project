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


def list_all_the_numbers_from_the_list(lst):
    for i in lst:
        return print(i) # returns only first item on the list

def list_all_the_numbers_from_the_list_2(lst):   
    for item in my_lst:
         print(item) # returns all, one under another 


def list_all_the_numbers_from_the_list_3(lst):
    result = []  # Create an empty list
    for i in lst:
        result.append(i)  # Add each item to the list
    return result  # Return the full list as a list

   
list_all_the_numbers_from_the_list(my_lst)
list_all_the_numbers_from_the_list_2(my_lst)
print(list_all_the_numbers_from_the_list_3(my_lst))


def reverse(lst):
    # Write code here
    for i in lst:  
        print(-lst)