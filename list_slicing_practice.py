""""
Create a program that receives a list as input (given) and prints the following sliced list:

For odd-length lists: take the middle item and one item on each side (3 items total)
For even-length lists: take the two middle items
When dividing numbers:

/ gives you a decimal number (5/2 = 2.5)
// removes the decimal part (5//2 = 2)
For this challenge, use // because list slicing only works with whole numbers.
"""

lst = [1,2,3,4,5,6,7,8,9,10]

if len(lst) % 2 == 0: # we check if the length of the list (len(lst)) is even by using the modulus operator (%). If the length is even, the condition will be true.
    # calculate the two middle items
    lst_mid = lst[len(lst)//2-1:len(lst)//2+1]
    # len(lst)//2 gives us the index of the first middle item.
    # len(lst)//2 - 1 gives us the index of the second middle item.
    # The slice lst[len(lst)//2-1:len(lst)//2+1] extracts the two middle items from the list.
else: # If the list length is odd, we take the middle item and one item on each side.
    lst_mid = lst[len(lst)//2-1:len(lst)//2+2] # The slice lst[len(lst)//2-1:len(lst)//2+2] extracts three items: the middle item and one item before and after it.
print(lst_mid) 
# Finally, we print the sliced list, which contains either two middle items (for even-length lists) or three items (for odd-length lists).
 
