"""Create a function named merge that receives two lists as arguments. 
The function merges the two lists into one sorted list and returns it.
For example the following arguments: merge([1, 4, 2], [2, 5, 9]) will return [1, 2, 2, 4, 5, 9]"""

list1 = [1, 4, 2]
list2 = [2, 5, 9]

def merge(lst1, lst2):
    res = []
    for i in range(len(lst2)):
        res.append(lst2[i])
    for i in range(len(lst1)):
        res.append(lst1[i])
    res.sort()
    return print(res)

merge(list1, list2)

"or"

def merge2(lst1, lst2):
    merged_list = lst1 + lst2  # Concatenating lists
    merged_list.sort()  # Sorting the merged list
    return print(merged_list)  # Returning the sorted list

merge2(list1, list2)
