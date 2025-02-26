"""
Create a program that receives a list of numbers as input and prints a new list that:

Contains the original list followed by its reverse
Has the first element of the original list inserted at the beginning and the last element inserted at the end
Repeats this entire sequence twice
"""

numbers = [1, 2, 3]

original_and_reverse = numbers + numbers[::-1]
first_element = [numbers[0]]
last_element = [numbers[-1]]
new_list = first_element + original_and_reverse + last_element
new_list_repeated = new_list * 2
print(new_list_repeated)
