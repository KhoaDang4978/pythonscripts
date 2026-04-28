# This is a bank account class
class Bank_Acc: 
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposit successfully!")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Invalid amount!")
        else: 
            self.balance -= amount
            print("Withdraw successfully!")
    def get_balance(self):
        print(f"Your balance is: ${self.balance}")
acc = Bank_Acc(1000)
acc.get_balance()
acc.deposit(500)
acc.get_balance()
acc.withdraw(200)
acc.get_balance()
acc.withdraw(99999)