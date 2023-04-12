'''
Dada una secuencia de datos en python (lista, tupla, cadena de caracteres). Utilizar
compresión de listas para convertir esa secuencia en una lista de tuplas, donde el
primer elemento de las tuplas será un índice en la colección y el segundo será su
valor. Ejemplos:
["examen", "de", "python"] - > [(1,"examen"), (2,"de"), (3,"python")]
("examen", "de", "python") - > [(1,"examen"), (2,"de"), (3,"python")]
'''
seq = ["examen", "de", "python"]

seq_result = [(i+1, seq[i]) for i in range(len(seq)]
print(seq)


