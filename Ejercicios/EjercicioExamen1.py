'''Escribe una función que emule el comportamiento de zip, tomando
como argumento cualquier número de secuencias y devolviendo una lista de
tuplas. Ejemplo: my_zip([10, 20,30], 'abc') deberá devolver [(10, 'a'), (20, 'b'), (30,'c')].'''

def my_zip (seq1 , seq2) :
    zippedList = []
    for i in range(seq1.len()):
        zippedList.append(tuple(seq1[i],seq2[i]))

    return zippedList

seq1 = [10, 20,30]
seq2 = 'abc'
print(my_zip(seq1,seq2))

