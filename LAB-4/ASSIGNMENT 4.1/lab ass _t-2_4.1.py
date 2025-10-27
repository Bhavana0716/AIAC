def factorial(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

try:
    num = int(input("Enter a positive integer: "))
    print(factorial(num))
except ValueError:
    print("Invalid input")