class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self):
        
        dp_d=int(input('top up your balance: '))
        self.balance+=dp_d
        print('current balance: '+str(self.balance))
    def withdraw(self):
        wd_d=int(input('enter the sum of withdraw: '))
        if self.balance>=wd_d:
            self.balance-=wd_d
            print('current balance: '+str(self.balance))
        else:
            print("Not accepted ")


owner=str(input('Name of the owner: '))
balance=int(input('Your balance is: '))
x=Account(owner,balance)
x.deposit()
x.withdraw()
