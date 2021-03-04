# Importing the class
from account import Account

class Saving_Acc(Account):
    def withdraw(self, allaccounts):
        withdrawer_name = input("Please enter the name of the withdrawer: ")
        if withdrawer_name:
            for x in allaccounts:
                if withdrawer_name == x.name:
                    a = int(input("How many months did the money stay the the account: "))
                    if a >= 6:
                        withdraw_amount = int(input("Please enter the amount you want to withdraw: "))
                        x.amount = x.amount - withdraw_amount
                        interest = withdraw_amount * (3 / 100)
                        print("As your money has stayed in your account for more that 1 month you will get "
                              "an interest of", interest)
                        print("New balance", x.amount + interest)
                    else:
                        print("Please note that you cannot withdraw, wait until you reach 6 months")
                else:
                    print("Please create an account, we can't find you in our system")
