from typing import Callable

def apply_discount(price: float, discount: float) -> float:
    """
    Calculates the final price after applying a percentage discount.

    This function ensures that the price is never negative and the discount is within the valid range (0 to 100).
    If the calculated final price is negative, it returns 0 to prevent illogical pricing.

    Args:
        price (float): The original price of the item. Must be non-negative.
        discount (float): The discount percentage to apply. Must be between 0 and 100.

    Returns:
        float: The price after discount. Returns 0 if the result is negative.

    Example:
        >>> apply_discount(100.0, 20.0)
        80.0
    """
    # Subtract the discount amount from the original price.
    # This prevents the final price from being negative due to excessive discounts.
    final: float = price - (price * discount / 100)
    # Defensive programming: Ensure the final price is not negative.
    if final < 0:
        final = 0.0
    return final

def get_price_input(prompt: str) -> float:
    """
    Prompts the user for a non-negative price value and validates the input.

    This function loops until the user provides a valid, non-negative price.
    It prevents negative pricing, which is not meaningful in most business contexts.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        float: A validated non-negative price value.
    """
    while True:
        try:
            value: float = float(input(prompt))
            # Negative prices are not allowed; prompt user again if entered.
            if value < 0:
                print("Price should never be negative. Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            # Handles non-numeric input gracefully.
            print("Invalid input. Please enter a valid number.")

def get_discount_input(prompt: str) -> float:
    """
    Prompts the user for a discount percentage between 0 and 100 and validates the input.

    This function ensures the discount is realistic and prevents illogical values
    such as negative discounts or discounts greater than 100%.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        float: A validated discount percentage between 0 and 100.
    """
    while True:
        try:
            value: float = float(input(prompt))
            # Discount must be within 0 to 100; otherwise, prompt user again.
            if value < 0 or value > 100:
                print("Discount should be between 0 and 100.")
                continue
            return value
        except ValueError:
            # Handles non-numeric input gracefully.
            print("Invalid input. Please enter a valid number.")

# Gather validated user input for price and discount.
price: float = get_price_input("Enter the price: ")
discount: float = get_discount_input("Enter the discount (%): ")

# Display the final price after applying the discount.
print("Final price after discount:", apply_discount(price, discount))