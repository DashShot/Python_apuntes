'''
● Definir una clase Matrix que permita trabajar con matrices algebraicas de un
modo más directo e intuitivo. Comportamiento:
    ○ sobrecargar operadores aritméticos (+, - )
    ○ sobrecargar operadores de asignación (+=, -=)
    ○ trasponer y consultar tamaño
    ○ sobrecargar operador ==
    ○ sobrecargar operador []
        ■ __getitem__
        ■ __setitem__
'''

class Matrix:

    def __init__(self,m ,n, value=0 ):
        self._m = m
        self._n = n
        self._rows = [[value] * n for _ in range(m)]

    def getm(self):
        return self._m

    def getn(self):
        return self._n

    def getrows(self):
        return self._rows
    def __add__(self, matrix):
        if matrix.getn() == self._n:
            if matrix.getm() == self._m:
                for i in range(self._n):
                    for j in range(self._m):
                        return Matrix(self._m,self._n,self._rows[i][j] + matrix.getrows()[i][j])
    def __sub__(self, matrix):
        if matrix.getn() != self._n:
            return False
        if matrix.getm() != self._m:
            return False


    def __str__(self):
        return f"({self._m}x{self._n}: {self._rows}"

if __name__ == "__main__":
    matrix1 = Matrix(3,3,4)
    matrix2 = Matrix(3,3,2)
    print(matrix1)
    print(matrix2)
    print(matrix1.__add__(matrix2))