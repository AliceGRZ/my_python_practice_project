"""Create a function named merge that receives two lists as arguments. 
The function merges the two lists into one sorted list and returns it.
For example the following arguments: merge([1, 4, 2], [2, 5, 9]) will return [1, 2, 2, 4, 5, 9]"""


def merge(lst1, lst2):
    res = []
    for i in range(len(lst2)):
        res.append(lst2[i])
    for i in range(len(lst1)):
        res.append(lst1[i])
    res.sort()
    return res


"or"

def merge(lst1, lst2):
    merged_list = lst1 + lst2  # Concatenating lists
    merged_list.sort()  # Sorting the merged list
    return merged_list  # Returning the sorted list


def combine_and_filter(lst, threshold):
    # Write code here
    for i in lst:
        if i <= threshold:
            lst.pop(i <= threshold)
        print(lst.sort())