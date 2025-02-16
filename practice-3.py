class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return self.balance
        
        elif self.balance < amount:
            print("insufficient funds!")

account = BankAccount()  
account.deposit(100)  
account.withdraw(50)  
print(account.balance) 