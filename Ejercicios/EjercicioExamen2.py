#    Escribe una función dict_partition que reciba como argumentos un
#    diccionario (d) y una función (f). dict_partition devolverá dos diccionarios, donde
#    cada uno contendrá pares clave-valor extraídos de d. La decisión de en cuál de
#    los dos diccionarios colocar cada par clave-valor dependerá de la salida de la
#    función f. f recibirá un par clave valor y devolverá True o False. Si devuelve True,
#    el par clave valor se insertará en el primer diccionario. Si devuelve False, en el
#    segundo.
#    Nota: solo se pide implementar la función dict_partition


def dict_partition(d, func):
    d1 = dict()
    d2 = dict()
    for key in d.keys():    #  Para acceder a las keys del diccionario
        if func(key):
            d1[key] = d[key]
        else:
            d2[key] = d[key]
    return d1, d2


def func(keys):
    if len(keys) > 2:
        return True
    return False


def main():
    d = {"valor1": 12, "v2": 3, "vaa3": 4}
    print(dict_partition(d, func))


main()