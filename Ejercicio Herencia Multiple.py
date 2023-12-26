class Vehiculo():
    def __init__(self,color,ruedas,ancho,alto,asientos):
        self.color = color
        self.ruedas=ruedas
        self.ancho=ancho
        self.alto=alto
        self.asientos=asientos
    
    def acelerar(self):
        return "Estoy acelerando"
    
    def frenar(self):
        return "Estoy frenando"
    
    def girar(self):
        return "Estoy girando"
    
class Furgoneta(Vehiculo):
    def __init__(self,color,ruedas,ancho,alto,asientos,aire_acondicionado,cilindrada):
        super().__init__(self,color,ruedas,ancho,alto,asientos)
        self.aire_acondicionado = aire_acondicionado
        self.cilindrada = cilindrada

    def cargar(self):
        return "Estoy cargando"
    
    def marcha_atras(self):
        return "Estoy dando marcha atras"
    
    def arrancar(self):
        return "Estoy arrancando"

class Coche(Vehiculo):
    def __init__(self,color,ruedas,ancho,alto,asientos,aire_acondicionado,cilindrada):
        super().__init__(self,color,ruedas,ancho,alto,asientos)
        self.aire_acondicionado = aire_acondicionado
        self.cilindrada = cilindrada

    def cargar(self):
        return "Estoy cargando"
    
    def marcha_atras(self):
        return "Estoy dando marcha atras"
    
    def arrancar(self):
        return "Estoy arrancando"
    
class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,ancho,alto,asientos,marchas):
        super().__init__(self,color,ruedas,ancho,alto,asientos)
        self.marchas = marchas

    def saltar(self):
        return "Estoy saltando"
    
    def derrapar(self):
        return "Estoy derrapando"
    
class Moto(Vehiculo):
    def __init__(self,color,ruedas,ancho,alto,asientos,marchas,cilindrada):
        super().__init__(self,color,ruedas,ancho,alto,asientos)
        self.marchas = marchas
        self.cilindrada = cilindrada

    def saltar(self):
        return "Estoy saltando"
    
    def derrapar(self):
        return "Estoy derrapando"