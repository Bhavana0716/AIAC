"""
Calculator for two numbers.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b. Error if b is zero."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == "+":
    print("Result:", add(x, y))
elif op == "-":
    print("Result:", subtract(x, y))
elif op == "*":
    print("Result:", multiply(x, y))
elif op == "/":
    print("Result:", divide(x, y))
else:
    print("Invalid operation")