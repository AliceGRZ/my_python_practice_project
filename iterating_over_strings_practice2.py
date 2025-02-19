""""
Create a program that receives a string as input, 
and it prints how many times the character p is in the string.
Some chars might be uppercase, use char.lower() to convert it to lowercase.
"""

text = "Happy people play ping pong"
# Option 1
count = 0
for char in text:
    if char.lower() == 'p':
        count += 1
print(count)

# Option 2
character = "P"
total = 0
# Count occurrences of 'p' (case-insensitive)
total = text.lower().count(character.lower())

print(total)