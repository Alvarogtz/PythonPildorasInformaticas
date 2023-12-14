personas=[]

while len(personas) < 10:
    try:
        entrada = input("Introduce nombre persona: ")

        if(personas.count(entrada) > 0):
            raise ValueError
        else:
            personas.append(entrada)

    except ValueError:
        print("Error. Este nombre ya se ha introducido")

print(personas)