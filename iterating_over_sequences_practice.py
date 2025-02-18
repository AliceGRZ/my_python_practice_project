""""
Iteration means going through elements one by one in a sequence. 
With lists, we can access each element systematically using different methods.
"""
words = "penguin,elephant,koala,tiger,dolphin,giraffe,kangaroo,zebra,lion,panda"
lst = words.split(",")
new_lst = []
for item in lst:
    if len(item) > 5:
        new_lst.append(item)
print(new_lst)