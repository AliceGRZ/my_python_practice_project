# first option
list = [1,2,3,4,5,6]
def sum_even_numbers_from_a_list(lst):
    no_lst = []
    for number in lst:
        if number % 2 == 0:
            no_lst.append(number)
    print(f"Even number from the list are: {no_lst}")
    
    total = 0
    for number in range(len(no_lst)):
        total += no_lst[number]
    print(f"Total amount of even numbers is: {total}")

sum_even_numbers_from_a_list(list)

# second option
numbers = [1,2,3,4,5,6]
even_sum = 0
for num in numbers:
    if int(num) % 2 == 0:
        even_sum += int(num)
print(even_sum)


