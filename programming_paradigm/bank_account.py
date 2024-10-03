# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize account balance
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            # Add amount to the account balance
            self.account_balance += amount
            return f"Deposited: {amount}"
        else:
            return "Error: Deposit amount must be positive."

    def withdraw(self, amount):
        if amount <= self.account_balance:
            # Deduct amount from the account balance
            self.account_balance -= amount
            return f"Withdrew: {amount}"
        else:
            return "Error: Insufficient funds."

    def display_balance(self):
        # Display the current account balance
        return f"Current balance: {self.account_balance}"

