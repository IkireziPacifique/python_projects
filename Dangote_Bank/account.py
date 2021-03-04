#Creation of class
class Account:
    # creating a constructor
    def __init__(self, name="", birth_date="", amount=0, account_number=""):
        self.name = name
        self.birth_date =birth_date
        self.amount = amount
        self.account_number = account_number

    # deposit method
    def deposit(self, AllAccounts):
        print("YEAAY YOU ARE DEPOSITING")
        depositor_name = input("Please enter the name of the depositor: ")
        if depositor_name:
            for x in AllAccounts:
                if depositor_name == x.name:
                    deposit_amount = int(input("Please enter the amount you want to deposit: "))
                    x.amount = x.amount + deposit_amount
                    print("New amount" , x.amount)
        else:
            print("Please create an account")

    # withdraw method
    def withdraw(self, allaccounts):
        withdrawer_name = input("Please enter the name of the withdrawer: ")
        if withdrawer_name:
            for x in allaccounts:
                if withdrawer_name == x.name:
                    withdraw_amount = int(input("Please enter the amount you want to withdraw: "))
                    x.amount = x.amount - withdraw_amount
                    print("New amount", x.amount)
        else:
            print("Please create an account")

    # view Accounts method
    def view(self, allaccounts):
        acc_no = 0
        for x in allaccounts:
            acc_no = acc_no + 1
            print("\nACCOUNT " , acc_no , "\n-----------")
            print("CLIENT'S NAME", x.name)
            print("CLIENT'S BIRTHDATE", x.birth_date)
            print("CURRENT AMOUNT", x.amount)
            print("ACCOUNT NUMBER", x.account_number)

    # transfer method
    def transfer(self, allaccounts):
        sender = input("Who is going to send money? ")
        if sender:
            for x in allaccounts:
                if sender == x.name:
                    receiver = input("Who is going to receive the money?")
                    if receiver:
                        for i in allaccounts:
                            if receiver == i.name:
                                amount_to_send = int(input("How much do you want to send: "))
                                x.amount = x.amount - amount_to_send
                                i.amount = i.amount + amount_to_send
                                print( "-" , x.name , "has successfully transfered " , amount_to_send ,
                                      ".His current balance is " , x.amount)
                                print( "-" , i.name , "has received" , amount_to_send , "from" , x.name ,
                                       ". His current balance is " , i.amount)
                                print("The transfer was successful!")
