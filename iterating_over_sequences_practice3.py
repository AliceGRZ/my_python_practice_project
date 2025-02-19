"""
Write a program that takes two inputs: a text string and a delimiter character. 
The program should split the text by whitespace into words,
 then join these words using the specified delimited character and print the resulting string.
"""

text = "What is it?"
delimiter = "-"
res = text.split()
res = delimiter.join(res)
print(res)