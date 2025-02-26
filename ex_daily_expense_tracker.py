print("Welcome to the Daily Expense Tracker!\n")

print("Menu:\n"
      "1. Add a new expense\n"
      "2. View all expenses\n"
      "3. Calculate total and average expense\n"
      "4. Clear all expenses\n"
      "5. Exit")

# Initialize an empty list to store expenses
expenses = []

while True:
    # Get user choice
    choice = input()
    
    if choice == "1":
        # Add a new expense
        amount = float(input())
        expenses.append(amount)
        print("Expense added successfully!")

    elif choice == "2":
        # View all expenses
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for index, expense in enumerate(expenses):
                print(f"{index + 1}. {expense}")
        
    elif choice == "3":
        # Calculate total and average expense
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            total = sum(expenses)
            average = total / len(expenses)
        print(f"Total expense: {total}")
        print(f"Average expense: {average}")
    
    elif choice == "4":
        # Clear all expenses
        expenses.clear()
        print("All expenses cleared.")
    elif choice == "5":
        # Exit the program
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    elif choice not in range(1,5):
        print("Invalid choice. Please try again.")




