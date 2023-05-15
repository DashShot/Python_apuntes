def plus_minus(lista):
    resultado = 0
    for i, num in enumerate(lista): # Para iterar sobre un numero y un indice
        if i == 0:
            resultado += num
        elif i % 2 == 0:
            resultado -= num
        else:
            resultado += num
    return resultado


print(plus_minus([10, 20, 30, 40, 50, 60]))