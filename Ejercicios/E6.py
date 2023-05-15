
def even_odd_sums(list):
    pares = 0
    impares = 0
    for i in range(len(list)):
        if i % 2 == 0:
            pares += list[i]
        else:
            impares += list[i]
    return pares, impares


print(even_odd_sums([10, 20, 30, 40, 50, 60]))