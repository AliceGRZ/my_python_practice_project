"""You are given a code which prints the numbers from 1 to 20 (including).

Your task is to add if and continue statements so that only the even numbers will be printed (2, 4, 6, ...). """


for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i)