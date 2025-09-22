def calculate_percentage(amount, percent):
    """Calculate the percentage value of a given amount."""
    return amount * percent / 100  # Multiply amount by percent and divide by 100

total_amount = 200  # The base amount to calculate percentage from
percentage_value = 15  # The percentage rate to apply

result = calculate_percentage(total_amount, percentage_value)  # Get the percentage value
print(result)  # Output the result to the console