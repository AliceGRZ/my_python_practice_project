
print("Bill Split Calculator")

bill_amount = float(input("Enter total bill amount: "))
tip_percentage = float(input("Enter tip precentage: "))
num_people = int(input("Enter number of people: "))

tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
amount_per_person = total_amount / num_people

print(f"Total amount to pay is: {total_amount}")
print(f"Amount per person is {amount_per_person}")

