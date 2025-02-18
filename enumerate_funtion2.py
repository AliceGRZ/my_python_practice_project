"""
Write a program that receives a list of words as input (given), 
and prints a list of the indices of the words that are either longer 
than 3 characters or start with the letter 'a' (case-sensitive).
To check if a string starts with some substring use: str.startswith("substring")
"""


lst = ["cat", "apple", "dog", "elephant", "ant"]
word_list = []
for index, word in enumerate(lst):
    if len(word) > 3 or word.startswith("a"):
        word_list.append(index)
print(word_list)

