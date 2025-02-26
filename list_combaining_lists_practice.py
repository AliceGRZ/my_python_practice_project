"""
Create a program that receives a list as input (given) and prints the following list that:

Contains the elements of the input list repeated 3 times
Has the first element of the original list inserted between each repetition
Is surrounded by the last element of the original list
"""

lst = [1,2]

step1 = lst * 3
separator = [lst[0]]
step2 = lst + separator + lst + separator + lst
border = [lst[-1]]
step3 = border + step2 + border
print(step3)


