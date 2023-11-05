class BankAccount :
    accounts=[]
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self,amount):
        self.balance += amount
        return self
    
    def withdraw(self,amount):
        if self.balance < amount :
            print("Insufficient funds: Charging a $5 fee")
            self.balance -=amount- 5
        else:
            self.balance -= amount
    
        return self
        
    
    def display_account_info(self):
        print(f"Balance : ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0 :
            self.balance += (self.balance * self.int_rate)

    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

acc1=BankAccount(.05,1000)
acc2=BankAccount(.01,5000)

acc1.deposit(100).deposit(300).deposit(40).withdraw(2000).yield_interest()
acc2.deposit(300).deposit(250).deposit(500).withdraw(400).yield_interest()

BankAccount.print_accounts()