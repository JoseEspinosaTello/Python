#this file will hold the classes for several different bank accounts.
class BankAccount:
    def __init__(self, initialAmmount, acctName): #set properties using the inizializer.
        self.balance = initialAmmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")