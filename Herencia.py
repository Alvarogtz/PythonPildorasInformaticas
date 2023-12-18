class Persona():

    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido=apellido
        self.edad=edad

    def getDatosPersonales(self):
        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad)

    def hablar(self):
        return "Estoy hablando"

    def pensar(self):
        return "Estoy pensando"

    def caminar(self):
        return "Estoy caminando"


class Estudiante(Persona):

    def __init__(self,nombre,apellido,edad,escuela):
        super().__init__(nombre,apellido,edad)
        self.escuela=escuela

    def estudiar(self):
        return "Estoy estudiando"
    
    def getDatosPersonales(self):
        return super().getDatosPersonales() + " Escuela: " + self.escuela



persona1 = Persona("Alvaro","Gomez",35)
estudiante1 = Estudiante("PEter","Anguila",38,"Estudiantes bien")

print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())