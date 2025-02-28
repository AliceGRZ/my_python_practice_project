"""
Create a function named frequency_counter that takes a list data_list as an argument. 
The function should count the frequency of each item in the list and return a dictionary where the keys are the unique 
items from the list and the values are the counts of how many times each item appears.

For example, if the input list is [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], the function should return a dictionary like this:
"""

def frequency_counter(data_list):
    # Write code here
    dic = {}
    for index, value in enumerate(data_list):
        frequency = data_list.count(value)
        dic[value] = frequency
    print(dic)

list = [1, "apple", 2, "apple", 1, "banana", 2, 2]

frequency_counter(list)

# SOLUTION 2
def frequency_counter(data_list):
    # Create an empty dictionary to store the frequencies
    frequency_dict = {}

    # Loop through the list and update the frequencies
    for item in data_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    # Return the frequency dictionary
    return frequency_dict