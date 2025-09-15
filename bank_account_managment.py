# Bank Account System in OOP style

#? creating a bank account (class)
class BankAccount:

    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def check_balance(self):
        print(f"Account balance: {self.balance}")

#! \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#? creating accounts (objects)

acc1 = BankAccount("200320251234", "Amr", 1750)
acc2 = BankAccount("200320254321", "Peter", 2600)

acc1.deposit(200)
acc1.withdraw(120)
acc1.check_balance()

acc2.deposit(5000)
acc2.withdraw(36000)
acc2.check_balance()
