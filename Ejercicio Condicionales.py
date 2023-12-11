entrada = float(input("Introduce tu renta: "))

texto = ""

if(entrada < 12000):
    texto = "A la renta " + str(entrada) + "  le corresponde un 7%"
elif(entrada<18000):
    texto = "A la renta " + str(entrada) + "  le corresponde un 15%"
elif(entrada<35000):
    texto = "A la renta " + str(entrada) + "  le corresponde un 21%"
elif(entrada<70000):
    texto = "A la renta " + str(entrada) + " le corresponde un 35%"
else:
    texto = "A la renta " + str(entrada) + " le corresponde un 45%"

print(texto)
    