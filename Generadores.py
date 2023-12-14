"Funcion de siempre"

def funcionPares(limite):
    num = 1
    numerosPares=[]


    while num < limite:
        numerosPares.append(num*2)
        num += 1

    return numerosPares

#print(funcionPares(6))

"Generador"

def generadorPares(limite):
    num = 1
    while num < limite:
        yield num*2
        num += 1


#print("Llamamos al generador ...")

pares = generadorPares(6)

"Imprime el primer valor"
#print(next(pares)) 

"Imprime el segundo valor"
#print(next(pares)) 

"""for i in pares:
    print(i)"""


" ------ RECORRIENDO GENERADORES -------- "

"Parametros indefinidos que se trataran como tupla"
"""def capitales_mundo(*ciudades):
    for capital in ciudades:
        for letraCapital in capital:
            yield letraCapital"""

 #yield from

def capitales_mundo(*ciudades):
    for capital in ciudades:
        #for letraCapital in capital:
            yield from capital

capitales = capitales_mundo("Madrid","Berlin","Roma","Pekin")

print(next(capitales))
print(next(capitales))
print(next(capitales))

