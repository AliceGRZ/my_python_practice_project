
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")


for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")


"""
The enumerate() function allows you to loop through a sequence 
(like a list, tuple, or string) while keeping track of the index position of each item.
"""

numbers = [80,4,99,36,34]
lst = list(map(int, input().split(",")))
new_lst = []
for index, num in enumerate(lst):
    if num < 50 or num % 5 == 0:
        new_lst.append(index)
print(new_lst)