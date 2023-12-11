""" 
Crea un programa de Python que pida 2 números por consola. 
El programa debe imprimir todos los números primos comprendidos entre los 2 números introducidos por consola.
Los números primos son aquellos que solo son divisibles por 1 y por ellos mismos.
"""

number1 = int(input("Introduce numero: "))
number2 = int(input("Introduce numero: "))


def isPrimo(number):
    for i in range(2,number):
        if(number%i == 0):
            return False
    return True

for i in range(number1,number2):
        if (isPrimo(i)):
            print ("Numero primo "  + str(i))