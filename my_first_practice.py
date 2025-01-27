print("Hello World") 

###### Variables types ######
my_first_int = 5
my_first_string = " Hello"
my_first_float = 4.55
my_first_boolean = True 

###### Formatting and math symbols ######
print(f"{my_first_int + my_first_float}" + my_first_string + f" { my_first_boolean}")
print("5 is equal to 4.55 - " + f"{my_first_int == my_first_float}")
print("5 is not equal to 4.55 - " + f"{my_first_int != my_first_float}")
print("4.55 is less or equal than 5 - " + f"{my_first_float <= my_first_int}")
print("5 is less or equal than 4.55 - " + f"{my_first_int <= my_first_float}")

###### List features  ######
shopping_list = ["chesse", "milk", "bread", "chocolate", "butter", "coffee", "sample", "mint tea", "sample"]
item_number = [1,5,6,3,4]

# Joining Lists together
the_list = shopping_list + item_number
print(the_list)

# Counting the number of the same item on the list
sample_item = shopping_list.count("sample")
print(sample_item)

# Veryfing if item exists on the list
is_there_and_item = "coffee" in shopping_list
print(is_there_and_item)

# Adding an item to a list
new_item = "wine"
shopping_list.append(new_item)
print(shopping_list)

# Adding an item in certain place
shopping_list.insert(3, "tomatoes")
print(shopping_list)

# Remove the last item
shopping_list.pop()
print(shopping_list)

# Remove certain item
shopping_list.remove("mint tea")
print(shopping_list)

# Verify the lenght of the list
items_taken = len(shopping_list)
if items_taken > 10:
    print(f"{items_taken}" + " Not enough bags")
else: print(f"{items_taken}" + " We can shop")

shopping_list.append("ham")
shopping_list.append("apple juice")

items_taken = len(shopping_list)
if items_taken > 10:
    print(f"{items_taken}" + " Not enough bags")
else: print(f"{items_taken}" + " We can shop")

###### Loops ######
for item in shopping_list:
    print(item)



