""""Create a function named combine_and_filter that receives 2 arguments:

First argument is a list of numbers
Second argument is an integer threshold value
The function should:

Filter out all numbers that are less than or equal to the threshold value
Sort the remaining numbers
Return the resulting list
For example, calling combine_and_filter([1, 5, 3, 2, 7, 4], 3) should return [4, 5, 7]."""

def combine_and_filter(lst, threshold):
    # Write code here
    filtered = []
    for i in range(0, len(lst)):
        if lst[i] > threshold:
            filtered.append(lst[i])
    filtered.sort()
    return print(filtered)

combine_and_filter([1, 5, 3, 8, 2, 7, 4, 6],4)