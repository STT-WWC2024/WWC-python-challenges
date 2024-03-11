# Create a class representing a simple bank account with deposit and withdraw methods.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f"${self.balance}"
    
    def deposit(self, amt):
        self.balance += amt
        return self.balance

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            return self.balance
        else:
            return ("Error, insufficient funds")


my_account = BankAccount(100)

# starting balance of $100
print("--- Starting balance ---")
print(f"Starting balance is: ${my_account.balance}")

# deposit $50
print("--- Depositing $50 ---")
new_balance = my_account.deposit(50)
print(f"Account balance is ${new_balance}")

# withdraw $10
print("--- Withdrawing $10 ---")
new_balance = my_account.withdraw(10)
print(f"Account balance is ${new_balance}")

# overdraw $150 (balance at this point is $140)
print("--- Overdrawing account ---")
new_balance = my_account.withdraw(150)
print(f"{new_balance}")
print(f"Current balance is: {my_account.balance}")
