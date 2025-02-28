def create_student_dict(name, age, major):
    # Write code here
    students_details = {"name": name,"age" : age, "major": major}
    return students_details

# SOLUTION 2
def create_student_dict(name, age, major):
    # Create an empty dictionary
    student_dict = {}

    # Add key-value pairs to the dictionary
    student_dict["name"] = name
    student_dict["age"] = age
    student_dict["major"] = major

    # Return the dictionary
    return student_dict

def get_capital(country_capitals, country_name):
    # Write code here
    return country_capitals[country_name]

def update_employee_info(employee_dict, key, value):
    # Update the dictionary with the new key and value
    employee_dict[key] = value
    
    # Return the updated dictionary
    return employee_dict

def update_inventory(inventory_dict, item, quantity):
    # Update the dictionary with the new item and quantity
    if item in inventory_dict:
        inventory_dict[item] += quantity
    else:
        inventory_dict[item] = quantity
    
    # Return the updated dictionary
    return inventory_dict

# Write code here
recipe_book = {"Pancakes": ["flour", "milk", "eggs", "sugar"],
"Salad":["lettuce", "tomato", "cucumber", "olive oil"]}
print(recipe_book["Pancakes"])

recipe_book["Smoothie"] = ["banana", "milk", "honey"]
recipe_book["Smoothie"] += ["blueberries"]

print(recipe_book)

# Step 1: Create the Recipe Book
recipe_book = {
    "Pancakes": ["flour", "milk", "eggs", "sugar"],
    "Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
}

# Step 2: Access Ingredients for "Pancakes"
print(recipe_book["Pancakes"])

# Step 3: Add a New Recipe
recipe_book["Smoothie"] = ["banana", "milk", "honey"]

# Step 4: Modify the "Smoothie" Recipe
recipe_book["Smoothie"].append("blueberries")

# Step 5: Print All Recipes
print(recipe_book)

# Write code here
students_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
keys = students_grades.keys()
print(f"Students: {keys}")
values = students_grades.values()
print(f"Grades: {values}")
students_grades["Diana"] = 92
bobs_grade = students_grades.get("Bob")
print(f"Bob's grade: {bobs_grade}")
updated_grades = students_grades.pop("Charlie")
print(f"Updated grades: {students_grades}")


def check_inventory(inventory, item):
    # Write code here
    for item, quantity in inventory.items():
        if item in inventory:
            print(f"{item} is in stock. Quantity: {quantity}")
        else:
            print(f"{item} not in stock.")

def check_inventory(inventory, item):
    # Write code here
    quantity = inventory.get(item)
    if item in inventory:
            print(f"{item} is in stock. Quantity: {quantity}")
    else:
        print(f"{item} is not in stock.")

def check_inventory(inventory, item):
    if item in inventory:
        return f"{item} is in stock. Quantity: {inventory[item]}"
    else:
        return f"{item} is not in stock."
    

def print_employee_details(employee_data):
    # Write code here
    for key, value in employee_data.items():
        print(f'{key}: {value}')
    if employee_data == {}:
        print("No data available")

def print_employee_details(employee_data):
    # Check if the dictionary is empty
    if not employee_data:
        print("No data available")
    else:
        # Loop through the dictionary and print each key-value pair
        for key, value in employee_data.items():
            print(f"{key}: {value}")

def print_product_details(product_data):
    # Write code here
    if not product_data:
        print('No product information available')
    for key, value in product_data.items():
        print(f"{key.title()}: {value}")


def print_product_details(product_data):
    # Write code here
    if not product_data:
        print('No product information available')
    for key, value in product_data.items():
        print(f"{key.capitalize()}: {value}")