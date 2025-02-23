"""
Slicing has another step parameter: lst[start:stop:step], For example consider this list:
"""
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Gets every second element from index 1 to 8:
print(numbers[1:8:2])
# Output: [1, 3, 5, 7]

# Gets every third element from index 2:
print(numbers[2::3])
# Output: [2, 5, 8]

#Slicing also supports negative indices.
#Counting from end:
print(numbers[-3:])
# Output: [7, 8, 9]
#Here, -3 means "start 3 positions from the end"

#Count until end:
print(numbers[:-2])    
# Output: [0, 1, 2, 3, 4, 5, 6, 7]
#Here, -2 means "stop 2 positions from the end" (exclusive)

#Reversing with negative step:
print(numbers[::-1])
# Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

"""
Empty space before first : means “start from beginning”
Empty space between : means “go until the end”
-1 means "move backwards one step at a time" 
"""


"""
Create a program that receives a list as input (given) and prints three new lists based on the following slicing operations:

A list containing every third element, starting from index 1 (the second element)
A list containing all the elements from the 6th element to the 1st in reverse order
A list containing every second element starting from the middle of the list to the end
"""
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(lst[1::3])
print(lst[5::-1])
print(lst[len(lst)//2::2])


slice1 = lst[1::3]
slice2 = lst[5::-1]
middle = len(lst)//2
slice3 = lst[middle::2]
print(slice1)
print(slice2)
print(slice3)