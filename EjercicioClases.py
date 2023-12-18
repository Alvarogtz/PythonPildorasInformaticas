class CuentaCorriente():
    accountNumber = ""
    name=""
    balance=0.0

    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def getInfo(self):
        return "Account Number: " + self.accountNumber + " - Name: " + self.name + " - Balance: " + str(self.balance)
    
    def addMoney(self,money):
        self.balance += money
    
    def takeOffMoney(self,money):
        self.balance-=money