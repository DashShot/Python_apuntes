
def ordenar_mayor(cad):
    return sorted(cad.lower().split()), max(cad.split(" "), key=len)


cadena = "Hola mi nombre es Aitor"
print(ordenar_mayor(cadena))