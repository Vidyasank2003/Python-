class BankAccount:
    def __init__(self,accountNo,balance):
        self.accountNo=accountNo
        self.balance=balance
    def deposite(self,ammount):
        if ammount>0:
            self.balance=self.balance+ammount
            return self.balance
    def withdraw(self,ammount):
        if ammount>0 and ammount<self.balance:
            self.balance=self.balance-ammount
            return self.balance
    def total_Balance(self):
        return self.balance
acc1=BankAccount("1236778",100000)
acc1.deposite(2000)

print(acc1.total_Balance())
acc1.withdraw(6000)

print(acc1.total_Balance())




