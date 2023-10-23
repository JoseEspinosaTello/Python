#this file will hold the classes for several different bank accounts.
class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmmount, acctName): #set properties using the inizializer.
        self.balance = initialAmmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")


    # add new method
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    #add deposit method
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit complete.")
        self.getBalance()

    # add a withdraw method

    # this method determines if there is enough money to complete the requested withdrawl
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of {self.balance:.2f}"
            )

    # withrawl method

    def withdraw(self, amount):
        # we are going to start with a try to catch an error if we raise the exception
        try: 
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBegining Transfer.. 🚀')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! ✅✅✅\n\n*********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌❌ {error}')


# start a new class that will use inheritance
# this class will give a 5% reward to any deposit

class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()

# add a savings account

class SavingsAcct(InterestRewardAcct):
    def __init__(self, initialAmmount, acctName): 
        super().__init__(initialAmmount, acctName)
        self.fee = 5 # 5 dollar fee for withdraw fromm this account

    #overide the original withdraw method
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print(f"\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')