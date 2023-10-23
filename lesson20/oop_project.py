from bank_accounts import *

# create an instance of a bank account
Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")


Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)


Jim = InterestRewardAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100) # with rewards account Jim will have an extra 5 dollars

Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100) # gets extra 5% because SavingsAccount inherits from InterestRewardAcct

Blaze.transfer(10000, Sara) # transfer interupted because he does not have enough money

Blaze.transfer(1000, Sara)

Sara.getBalance()