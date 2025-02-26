"""
Create a program that receives two lists and prints a new list of all elements that are in the first list but NOT in the second list.
"""
lst1 = [1,2,3,4,5]
lst2 = [2,4,6]


for element in lst1:
    if element in lst2: 
        lst1.remove(element)
print(lst1)


result = []
for element in lst1:
    if element not in lst2:
        result.append(element)
print(result)
  



