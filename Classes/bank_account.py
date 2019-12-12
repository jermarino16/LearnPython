# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money
        
        return self.balance
    
    def withdraw(self, withdrawal):
        self.balance = self.balance - withdrawal
        
        return self.balance

jeremy_account = BankAccount("Jeremy", 100)
print(jeremy_account.balance)
jeremy_account.deposit(100)

print(jeremy_account.balance)
jeremy_account.withdraw(50)

print(jeremy_account.balance)