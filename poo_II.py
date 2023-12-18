class Persona():
    __nombre=""
    apellido=""
    __edad=0
    genero="sin definir"

    def __init__(self,nombre,apellido,genero):
        self.__nombre = nombre
        self.apellido = apellido
        self.genero = genero


    def hablar(self):
        return "La persona que se llama " + self.__nombre + " está hablando."
    
    def caminar(self):
        return "La persona que se llama " + self.__nombre + " está caminando."
    
    def getDatos(self):
        return "Nombre: " + self.__nombre + " Apellido: " + self.apellido + \
            " Edad: " + str(self.__edad) + " Genero: " + self.genero
    
    def setEdad(self,edad):
        if(edad > 0 and edad < 101):
            self.__edad=edad
        else:
            print("Error en la edad")

    

p1 = Persona("Alvaro","Zabala","Masculino")
p1.setEdad(25)

#print (p1.hablar())
print(p1.getDatos())
