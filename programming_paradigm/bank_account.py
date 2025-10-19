class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount < 0:
            print("You cannot deposit a negative amount")
            return False
        
        self.account_balance = amount + self.account_balance
        return True
    
    def withdraw(self, amount):
        if amount < 0:
            print("You cannot withraw a negative amount")
            return False
        elif amount > self.account_balance:
            return False
        else:
            self.account_balance = self.account_balance - amount
            return True
        
    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance)}")