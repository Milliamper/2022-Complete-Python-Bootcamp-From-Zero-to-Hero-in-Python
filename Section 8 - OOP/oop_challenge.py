'''
Create a bank account that has two attributes:
    owner
    balance
and two methods:
    deposit
    withdraw
Withdrawals may not exceed the available balance
'''

class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficiend founds")
        else:
            self.balance = self.balance - amount
            return self.balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def __str__(self):
        return f"{self.owner} has {self.balance} Ft"
    
acc1 = Account("Márton", 20000)
print(acc1)

acc1.deposit(30000)
print(acc1)

acc1.withdraw(50000)
print(acc1)



