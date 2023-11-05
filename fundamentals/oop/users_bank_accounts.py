class user :
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = {
            "acc1" :BankAccount(0.5,2000),
            "acc2" : BankAccount(0.2,3000)
        }
    def make_deposit(self,amount):
        BankAccount.deposit(amount)
        return self
    
    def make_withdrawal(self,amount):
        BankAccount.withdraw(amount)
        return self
        
    
    def display_user_balance(self):
        print(f"Mr {self.first_name} {self.last_name},acc1 Balance : ${self.account_balance['acc1'].display_account_info()}")
        print(f"Mr {self.first_name} {self.last_name},acc2 Balance : ${self.account_balance['acc2'].display_account_info()}")
    
    
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
        #print(f"Balance : ${self.balance}")
        return self.balance
    
    def yield_interest(self):
        if self.balance > 0 :
            self.balance += (self.balance * self.int_rate)

    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

zied=user('Zied','Riahi')
zied.account_balance['acc1'].deposit(100).deposit(300).deposit(40).withdraw(2000)
zied.account_balance['acc2'].deposit(200).deposit(400).deposit(450).withdraw(3000)
zied.display_user_balance()

ali=user('Ali','Tounsi')
ali.account_balance['acc1'].deposit(500).deposit(200).deposit(400).withdraw(1200)
ali.account_balance['acc2'].deposit(300).deposit(400).deposit(450).withdraw(800)
ali.display_user_balance()