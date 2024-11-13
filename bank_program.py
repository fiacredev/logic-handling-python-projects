class BankAccount:
  def __init__(self,account_holder,initial_balance = 0):
        self.account_holder = account_holder
        self.balance = initial_balance

  def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} new balane is {self.balance}")
        else:
            print("Amount to be deposited must be positive")
    
  def withdraw(self,amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawed ${amount} new balance is {self.balance}")
            else:
                print("Insufficient balance to be withdrawed")
        else:
            print("Amount withdrawed must be positive")

  def check_balance(self):
        print(f"Account Holder:{self.account_holder}")
        print(f"Current balance:{self.balance}")


account = BankAccount("kevin",100)
account.deposit(30)
account.withdraw(10)
account.check_balance()