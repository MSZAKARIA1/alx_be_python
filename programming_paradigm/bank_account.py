class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize account balance
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            # Add amount to the account balance
            self.account_balance += amount
            return f"Deposited: ${amount:.2f}"
        else:
            return "Error: Deposit amount must be positive."

    # def withdraw(self, amount):
    #     """Withdraw the specified amount from the account, if funds are sufficient."""
    #     if amount > 0:
    #         if amount <= self.account_balance:
    #             # Deduct amount from the account balance
    #             self.account_balance -= amount
    #             return f"Withdrew: ${amount:.2f}"
    #         else:
    #             print("Insufficient funds.")
    #     else:
    #         return "Error: Withdrawal amount must be positive."
    def withdraw(self, amount):
    """Withdraw the specified amount from the account, if funds are sufficient."""
    if amount > 0:
        if amount <= self.account_balance:
            # Deduct amount from the account balance
            self.account_balance -= amount
            return f"Withdrew: ${amount:.2f}"
        else:
            return "Insufficient funds."  # Return message instead of print
    else:
        return "Error: Withdrawal amount must be positive."


    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")

