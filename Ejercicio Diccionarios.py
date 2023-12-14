
pais = ""
paisesCiudades={}

def incluirPaisCiudad(pais,ciudad):
    existe = False
    for key,value in paisesCiudades.items():
        if pais == key:
            existe = True
            value.append(ciudad)
            break

            
    if existe == False:        
        paisesCiudades[pais] = [ciudad]


while(pais != "salir"):
    pais = input("Introduce pais: ")

    if(pais != "salir"):
        ciudad =  input("Introduce ciudad: ")
        incluirPaisCiudad(pais,ciudad)

print (paisesCiudades)
    