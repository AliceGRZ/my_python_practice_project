my_lst = [1, 2, 3, 4, 5, 6]

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
print(my_lst)