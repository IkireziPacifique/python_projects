# Importing the class
from account import Account

class Current_Acc(Account):
    def withdraw(self, allaccounts):
        withdrawer_name = input("Please enter the name of the withdrawer: ")
        if withdrawer_name:
            for x in allaccounts:
                if withdrawer_name == x.name:
                    withdraw_amount = int(input("Please enter the amount you want to withdraw: "))
                    x.amount = x.amount - withdraw_amount
                    a = int(input("How many months did the money stay the the account: "))
                    if a >= 1:
                        interest = withdraw_amount * (1/100)
                        print("As your money has stayed in your account for more that 1 month you will get "
                              "an interest of" , interest)
                        print("New balance", x.amount + interest)
                    else:
                        print("New balance", x.amount)
        else:
            print("Please create an account, we can't find you in our system")