# Bank Account System in OOP style

#? creating a bank account (class)
class BankAccount:

    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self):
        while True:
            amount = input("Enter amount to Deposit: ")
            if amount.isnumeric():
                amount = int(amount)
                break
            else:
                print("Invalid Entry, Try again, (Q)Exit.")
                if amount.upper() == "Q":
                    return
        self.balance += amount
        print(f"${amount} has been deposited into your account ending in ..{self.account_number[8:12]}")
        return amount

    def withdraw(self):
        while True:
            amount = input("Enter amount to Withdraw: ")
            if amount.isnumeric():
                amount = int(amount)
                break
            else:
                print("Invalid Entry, Try again, (Q)Exit.")
                if amount.upper() == "Q":
                    return
        if amount > self.balance:
            print("Insufficient Funds, Transaction declined.")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account ending in ..{self.account_number[8:12]}, New balance: ${self.balance}")
        return amount


    # def check_balance(self):
    #     return self.balance

#! \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#? creating accounts (objects)
acc1 = BankAccount("200320251234", "Amr", 5000)
# acc2 = BankAccount("200320255678", "Mona", 6000)


# Menu
menu_dict = {
    "1" : "Show account Info",
    "2" : "Deposit",
    "3" : "Withdraw",
    "4" : "Check Balance"
}

for key, val in menu_dict.items():
    print(f"{key}- {val}")

# Prompt User to choose Function
while True:
    prompt = input("> ").upper()
    if prompt not in ["1","2","3","4", "Q"]:
        print("Invalid Entry, Try again. Q(Exit)")
    else:
        break

methods_dict = {
    "2" : acc1.deposit,
    "3" : acc1.withdraw,
}

if prompt != "Q" and prompt in methods_dict.keys():
    methods_dict[prompt]()
elif prompt != "Q" and prompt not in methods_dict.keys():
    if prompt == "1":
        print(f"Here's Your Account Info => ACC#: {acc1.account_number}\nACC Holder:{acc1.owner}\nBalance: ${acc1.balance}")
    elif prompt == "4":
        print(f"Balance: ${acc1.balance}")
else:
    print("Exiting Bank System.....")

