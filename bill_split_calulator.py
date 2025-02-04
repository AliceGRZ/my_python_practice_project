"""
Here is a table that shows how to cast to different types:

Cast	Explanation
int()	Convert to a whole number
float()	Convert to a real number
bool()	Convert to a boolean
str()	Convert to a string
"""
print("Bill Split Calculator")
amountToPay = int(input("Please enter amount to pay: "))
tip = float(input("Please enter the tip :"))
numberOfpeople = int(input("Please enter number of people "))

if numberOfpeople == numberOfpeople:
    print(f"Amount for each person to pay is: {(amountToPay+ tip) / numberOfpeople }")
