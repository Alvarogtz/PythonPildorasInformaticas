import random

resultado = random.randint(1,100)
intentos = 0
numero = 0

try:
    numero = int(input("Introduce un numero entre 1 y 100: "))
except ValueError:
    print("Dato introducido incorrecto")

intentos += 1

while resultado != numero:
    try:
        if(numero < 0 or numero > 100):
            numero = int(input("Numero incorrecto. Introduce un numero entre 1 y 100: "))
        else:
            if(numero < resultado):
                numero = int(input("El numero es mayor. Prueba de nuevo: "))
            else:
                numero = int(input("El numero es menor. Prueba de nuevo: "))
    except ValueError:
        print("Dato introducido incorrecto")
        
    intentos+=1


print("Correcto! El numero a adivinar era el " + str(resultado) + ". Necesitaste " + str(intentos) + " intentos")