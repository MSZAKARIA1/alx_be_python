class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.account_balance += amount
        print(f"Deposited: ${amount}. New balance: ${self.account_balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.account_balance:
            print(f"Can't Withdraw: ${amount}. Try to withdraw a lower amount!")
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.account_balance}.")

    def display_balance(self):
        print(f"Your balance is: ${self.account_balance}.")
