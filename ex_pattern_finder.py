"""
Create a program that receives two lists of strings as input (given) and determines if the second list appears as a 
pattern within the first list (in consecutive order).

A pattern exists when all elements of the second list appear together, in the same order, 
somewhere within the first list, like finding a substring within a string.
"""

lst1 = [1,2,3,4,5,6,7]
lst2 = [3,4,5]

"""lst1 = [5,6,7,8,9]
lst2 = [6,8]"""

# If pattern is longer than the list, return False
if len(lst2) > len(lst1):
    print(False)
else:
    # Initialize result as False
    found = False
    
    # Check each possible starting position in lst1
    for i in range(len(lst1) - len(lst2) + 1):
        # Check if current slice matches pattern
        matches = True
        for j in range(len(lst2)):
            if lst1[i + j] != lst2[j]:
                matches = False
                break
        
        # If we found a match, update found and break
        if matches:
            found = True
            break
    
    print(found)
                
