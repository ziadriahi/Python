class user :
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
        
    
    def display_user_balance(self):
        print(f"Mr {self.first_name} {self.last_name} Balance : ${self.account_balance}")
    
    def transfer_money(self,receiver,amount):
        self.account_balance -= amount
        receiver.account_balance += amount
        self.display_user_balance()
        receiver.display_user_balance()

zied=user('Zied','Riahi')
zied.make_deposit(1000).make_deposit(300).make_deposit(450).make_withdrawal(700).display_user_balance()

mohamed=user('Mohamed','MED')
mohamed.make_deposit(2000).make_deposit(450).make_withdrawal(450).make_withdrawal(700).display_user_balance()

ali=user('Ali','TOUNSI')
ali.make_deposit(3000).make_withdrawal(100).make_withdrawal(700).make_withdrawal(550).display_user_balance()


zied.transfer_money(ali,500)