#Author Pacifique Linda IKIREZI
#Question 2 Dangote Bank

# Importing the Bank account class
from account import Account

# Importing the current account class
from current import Current_Acc

# Importing the current account class
from saving import Saving_Acc

# Creating accounts collection
allaccounts = []

# Inserting existing accounts
allaccounts.append(Account("Dangote", "1881", 1000, "ACC001922_TY"))
allaccounts.append(Account("Whites", "1900", 500, "ACC001922_AU"))
allaccounts.append(Account("Omondi", "1901", 100, "ACC001922_RW"))

# Ask the user the account they want to use
print("\n-------Dangote Bank-------")
print("PLEASE LET US KNOW THE ACCOUNT YOU HAVE BY CHOOSING FROM BELOW:")
print("1. CURRENT ACCOUNT")
print("2. SAVING ACCOUNT")
print("3. None from the above I am the manager")
accounts = int(input("WHICH OPERATION DO YOU WANT TO MAKE:"))

# Output for current account
if accounts == 1:
    print("")
    print("1. DEPOSIT")
    print("2. WITHDRAW")
    print("3. TRANSFER MONEY")
    operation = int(input("WHICH OPERATION DO YOU WANT TO MAKE: "))
    if operation == 1:
        current_deposit = Current_Acc()
        current_deposit.deposit(allaccounts)
    if operation == 2:
        current_withdraw = Current_Acc()
        current_withdraw.withdraw(allaccounts)
    if operation == 3:
        current_transfer = Current_Acc()
        current_transfer.transfer(allaccounts)

# Output for saving account
if accounts == 2:
    print("1. DEPOSIT")
    print("2. WITHDRAW")
    print("3. TRANSFER MONEY")
    operation = int(input("WHICH OPERATION DO YOU WANT TO MAKE: "))
    if operation == 1:
        saving_deposit = Saving_Acc()
        saving_deposit.deposit(allaccounts)
    if operation == 2:
        saving_withdraw = Saving_Acc()
        saving_withdraw.withdraw(allaccounts)
    if operation == 3:
        saving_transfer = Saving_Acc()
        saving_transfer.transfer(allaccounts)
# Output for the main account
if accounts == 3:
    print("1. DEPOSIT")
    print("2. WITHDRAW")
    print("3. VIEW ALL ACCOUNTS")
    print("4. TRANSFER MONEY")
    operation = int(input("WHICH OPERATION DO YOU WANT TO MAKE: "))
    if operation == 1:
        deposit = Account()
        deposit.deposit(allaccounts)
    if operation == 2:
        withdraw = Saving_Acc()
        withdraw.withdraw(allaccounts)
    if operation == 3:
        view = Account()
        view.view(allaccounts)
    if operation == 4:
        transfer = Account()
        transfer.transfer(allaccounts)