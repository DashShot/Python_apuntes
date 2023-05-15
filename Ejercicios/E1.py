import random


def guessing_name():
    nrand = random.randint(0, 100)
    print(f"Numero aleatorio:", {nrand})
    while True:
        respuesta = int(input("¿Cual es el númer0? "))
        if respuesta > nrand:
            print("Incorrecto el Numero es más pequeño")
        elif respuesta < nrand:
            print("Incorrecto el Numero es más grande")
        else:
            print("Correcto")
            break


guessing_name()
