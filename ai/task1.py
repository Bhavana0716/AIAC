def sum_even_odd(numbers):
    """
    This function adds up all the even numbers and all the odd numbers in the list.
    You give it a list of numbers, and it tells you the total of the evens and the total of the odds.
    Returns both sums as a pair.
    """
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

even, odd = sum_even_odd(numbers)
print("Sum of even numbers:", even)
print("Sum of odd numbers:", odd)