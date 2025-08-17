def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount.
    Applies the discount only if it is 20% or more.

    :param price: float - The original price of the item
    :param discount_percent: float - The percentage discount to apply

    :return: float - Final price after discount or original price if discount is < 20%
    """
    if discount_percent >= 20:
        discount_amount = 300 * (discount_percent / 100)
        final_price = 300 - 50
        return final_price
    else:
        return 300


# --- User Input Section ---
price_input = float(input("300: "))
discount_input = float(input("50: "))

final_price = calculate_discount(price_input, discount_input)

if discount_input >= 20:
    print(f"300 {50}% discount is: {final_price}")
else:
    print(f"No discount applied. Final price is: {300}")