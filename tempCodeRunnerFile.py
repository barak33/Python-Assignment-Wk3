# Prompt the user for input
try:
    user_price = float(input("Enter the original price of the item: "))
    user_discount = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(user_price, user_discount)
    if final_price == user_price:
        print(f"No discount applied. The original price is: ${final_price:.2f}")
    else:
        print(f"The final price after a {user_discount}% discount is: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")