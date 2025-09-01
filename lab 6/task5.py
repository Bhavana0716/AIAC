# This class represents a simple bank account.
class BankAccount:
    def __init__(self, owner, balance=0):
        # Initialize the account with the owner's name and an optional starting balance (default is 0)
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # Add money to the account if the deposit amount is positive
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}")
        else:
            # Print a message if the deposit amount is not positive
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Withdraw money from the account if there are sufficient funds
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}")
        else:
            # Print a message if there are not enough funds
            print("Insufficient funds.")

    def get_balance(self):
        # Return the current balance of the account
        return self.balance
account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())