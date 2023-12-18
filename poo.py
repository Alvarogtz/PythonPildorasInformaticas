class Coche():
    ruedas=4
    largoChasis=260
    anchoChasis=130
    arrancado=False

    def arrancar(self):
        self.arrancado=True

    def estadoCoche(self):
        if(self.arrancado):
            #print("El coché está arrancado")
            return "El coché está arrancado"
        else:
            #print("El coché NO está arrancado")
            return "El coché NO está arrancado"


mazda = Coche()
renault = Coche()


print("Tu coche tiene " + str(mazda.ruedas) + " ruedas.")
renault.arrancar()
print(renault.estadoCoche())
