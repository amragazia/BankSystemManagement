# Bank Account System in OOP style

import sys
import json

#? creating a bank account (class)
class BankAccount:

    def __init__(self, account_number, pin, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def check_balance(self):
        return self.balance
    
#! \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#? creating accounts (objects) (Update: create accounts in file.txt and reading from it)
# acc1 = BankAccount("200320251234", "Amr", 5000)
# acc2 = BankAccount("200320255678", "Mona", 6000)

accounts = [] #empty list(will have BankAccount Objects)

with open("list.json", "r") as f:
    data = json.load(f)

for acc in data:
    account = BankAccount(
        acc["account_number"],
        acc["pin"],
        acc["owner"],
        acc["balance"]
    )
    accounts.append(account)

#Persisting Changes Back to JSON File
def update_bank_accounts_list():
    data = []
    for acc in accounts:
        data.append({
            "account_number" : acc.account_number,
            "pin" : acc.pin,
            "owner" : acc.owner,
            "balance" : acc.balance
        })

    with open("list.json", "w") as f:
        json.dump(data, f, indent=4)


def authenticate():
    while True:
        get_acc_num = input("Enter your account number: ")
        if get_acc_num.isnumeric():
            break
        else:
            print("Invalid entry, try again.")

    for acc in accounts:
        if get_acc_num == acc.account_number:
            while True:
                get_pin = input("Enter your account pin: ")
                if get_pin.isnumeric():
                    break
                else:
                    print("Invalid entry, try again.")
            if get_pin == acc.pin:
                return True, acc
            else:
                print("Incorrect PIN.")
                return False, None
    print("No records found for entered account number.")
    return False, None

def session_control():
    while True:
        user_input = input("Start New session (Y/N): ").upper()
        if user_input not in ["Y", "N"]:
            print("Invalid entry, try again.")
        else:
            break
    if user_input == "Y":
        return True
    else:
        return False


is_authenticated, acc1 = authenticate()

if is_authenticated:
        

    start_session = True
    while start_session:

        menu_dict = {
            "1" : "Show account Info",
            "2" : "Deposit",
            "3" : "Withdraw",
            "4" : "Check Balance",
            "Q" : "Exit"
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

        if prompt == "1":
                print(f"Here's Your Account Info:\nACC#: {acc1.account_number}\nACC Holder: {acc1.owner}\nBalance: ${acc1.balance}")
        elif prompt == "2":
            while True:
                amount = input("Enter amount to Deposit: ")
                if amount.isnumeric() and int(amount) > 0:
                    amount = int(amount)
                    break
                else:
                    print("Invalid Entry, Try again, (Q)Exit.")
                    if amount.upper() == "Q":
                        sys.exit()
            acc1.deposit(amount)
            update_bank_accounts_list()  # save right away
            print(f"${amount} has been deposited into your account ending in ..{acc1.account_number[8:12]}, New balance: ${acc1.balance}")

        elif prompt == "3":
            while True:
                amount = input("Enter amount to Withdraw: ")
                if amount.isnumeric() and int(amount) > 0:
                    amount = int(amount)
                    break
                else:
                    print("Invalid Entry, Try again, (Q)Exit.")
                    if amount.upper() == "Q":
                        sys.exit()
            if not acc1.withdraw(amount):
                print("Insufficient Funds, Transaction declined.")
            else:
                update_bank_accounts_list()   # save right away
                print(f"${amount} has been withdrawn from your account ending in ..{acc1.account_number[8:12]}, New balance: ${acc1.balance}")

        elif prompt == "4":
            balance = acc1.check_balance()
            print(f"You're available balance: ${balance}")

        elif prompt == "Q":
            break
        

        start_session = session_control()


update_bank_accounts_list()

