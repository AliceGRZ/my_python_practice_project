"""Create a function named calculate_discount that takes two parameters:

price: The original price of an item (float)
discount_percentage: The discount percentage (float)
The function should:

Calculate the discount amount
Subtract the discount amount from the original price
Round the result to 2 decimal places
Return the final discounted price
For example, if the original price is $100 and the discount is 20%, the function should return $80.00."""


def calculate_discount(price, discount_percentage):
    # Write code here
    price = float(input())
    discount_percentage = float(input())

    discount_amount = (discount_percentage / 100) * price
    new_price = price - discount_amount
    new_price_rounded = round(new_price, 2)
    return new_price_rounded

print(calculate_discount(100, 20))


# SOLUTION 2

def calculate_discount(price, discount_percentage):
    discount_amount = price * (discount_percentage / 100)
    discounted_price = price - discount_amount
    return round(discounted_price, 2)
      