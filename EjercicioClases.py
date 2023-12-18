class CuentaCorriente():
    accountNumber = ""
    name=""
    balance=0.0

    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def getInfo(self):
        return "Account Number: " + self.accountNumber + " - Name: " + self.name + "- Balance: " + str(self.balance)
    
    def addMoney(self,money):
        self.balance += money
    
    def takeOffMoney(self,money):
        self.balance-=money


cuenta1 = CuentaCorriente("123456789","Alvaro",0)

print(cuenta1.getInfo())
cuenta1.addMoney(758.62)
print(cuenta1.getInfo())
cuenta1.takeOffMoney(58.25)
print(cuenta1.getInfo())
