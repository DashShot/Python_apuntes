'''Escribe una función que emule el comportamiento de zip, tomando
como argumento cualquier número de secuencias y devolviendo una lista de
tuplas. Ejemplo: my_zip([10, 20,30], 'abc') deberá devolver [(10, 'a'), (20, 'b'), (30,'c')].'''


def my_zip(*args):  # culaquier numero de args
    zipped_list = []
    min_length = min(len(seq) for seq in args)
    for i in range(min_length):
        tup = tuple(seq[i] for seq in args)
        zipped_list.append(tup)

    return zipped_list


seq1 = [10, 20, 30]
seq2 = 'abc'
print(my_zip(seq1, seq2))
