from EjercicioClases import CuentaCorriente

class CuentaJoven(CuentaCorriente):
    
    def __init__(self,accountNumber,name,balance,__bonus_promocion):
        super().__init__(accountNumber,name,balance)
        self.__bonus_promocion=__bonus_promocion
        self.balance += self.__bonus_promocion
    
    def getBonus(self):
        return self.__bonus_promocion
    
    def getInfo(self):
        return super().getInfo() + " Bonus: " + str(self.getBonus())
    

cuenta1=CuentaCorriente("142536","Juan",458.65)
print(cuenta1.getInfo())
cuenta1.addMoney(150)
print(cuenta1.getInfo())
cuenta1.takeOffMoney(95)
print(cuenta1.getInfo())


cuentaJoven1=CuentaJoven("478596321","Paco",1025.69,455.25)
print("Bonus: " + str(cuentaJoven1.getBonus()))
print(cuentaJoven1.getInfo())
    