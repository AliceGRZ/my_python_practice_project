"""
Write a program that receives three inputs (given):

 A list of prices
A list of item names
A budget per item
 

The program should print:

A list of items that you can afford within your budget
How much budget would you need if you bought all of the affordable items
How many items you couldn't afford
"""


prices = [10,25,5,15]
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = ["hammer","saw","nails","brush"]
budget_per_item = 12

affordable_items = []
cant_afford = 0
total_needed = 0
non_affordable = []

# SOLUTION 1
for index, price in enumerate(prices):
        if budget_per_item >= price:
            affordable_items.append(items[index])
            total_needed += price
        elif budget_per_item < price:
             non_affordable.append(index)
             cant_afford = len(non_affordable)

print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)


# SOLUTION 2
affordable_items = []
cant_afford = 0
total_needed = 0


for i in range(len(prices)):
    if prices[i] <= budget_per_item:
        affordable_items.append(items[i])
        total_needed += prices[i]
    else:
        cant_afford += 1


print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)
 
           

            
        


