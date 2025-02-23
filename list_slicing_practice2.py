"""
Create a program that takes a list and prints:

For lists with 5 or more items: the first two and last two items
For lists with less than 5 items: the first and last item only
"""

input_list = ["a", "b", "c", "d", "e"]

if len(input_list) >= 5:
    first_two = input_list[:2]
    last_two = input_list[-2:]
    new_list = first_two + last_two
    print(new_list)
if len(input_list) <= 5:
    first_two = input_list[:1]
    last_two = input_list[-1:]
    new_list = first_two + last_two
    print(new_list)



if len(input_list) >= 5:
    print(input_list[:2] + input_list[-2:])
else:
    print([input_list[0], input_list[-1]])
