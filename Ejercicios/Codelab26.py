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

    def __init__(self, m, n, value=0):
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
                        return Matrix(self._m, self._n, self._rows[i][j] + matrix.getrows()[i][j])

    def __sub__(self, matrix):
        if matrix.getn() != self._n:
            raise Exception("No es posible restar matrices de distinto rango")
        if matrix.getm() != self._m:
            raise Exception("No es posible restar matrices de distinto rango")

    def __str__(self):
        return f"({self._m}x{self._n}: {self._rows}"


if __name__ == "__main__":
    matrix1 = Matrix(3, 3, 4)
    matrix2 = Matrix(3, 3, 2)

    print(matrix1)
    print(matrix2)
    print(matrix1.__add__(matrix2))
    matrix3 = matrix1 + matrix2
    print(matrix3)
'''
SOL:
class Matrix :
     def __init__ (self , m, n, value= 0):
        self .m = m
        self .n = n
        self ._rows = [[value] * n for _ in range (m)]
     
     def __getitem__ (self , idx):
        return self ._rows[idx]
        
    def __setitem__ (self , idx, item):
        self ._rows[idx] = item
 
    def __str__ (self ):
        s = '\n'.join([ ' '.join([ str(item) for item in row]) for row in self ._rows])
        return s + '\n'
 
    def transpose (self ):
        self .m, self .n = self .n, self .m
        self ._rows = [ list (item) for item in zip(*self ._rows)]
 
    def get_rank (self ):
        return self .m, self .n
 
    def __eq__ (self , mat):
        return mat._rows == self ._rows
 
    def __add__ (self , mat):
        if self .get_rank() != mat.get_rank():
        raise Exception ("Trying to add matrixes of varying rank!")
        ret = Matrix( self .m, self .n)
        for x in range (self .m):
            row = [ sum(item) for item in zip(self ._rows[x], mat[x])]
            ret[x] = row
            return ret
 
    def __sub__ (self , mat):
        if self .get_rank() != mat.get_rank():
            raise Exception ("Trying to add matrixes of varying rank!")
        ret = Matrix( self .m, self .n)
        for x in range (self .m):
            row = [item[ 0] - item[ 1] for item in zip(self ._rows[x], mat[x])]
            ret[x] = row
            return ret
 
    def __iadd__ (self , mat):
         temp_mat = self + mat
         self ._rows = temp_mat._rows[:]
         return self
 
    def __isub__ (self , mat):
        temp_mat = self - mat
        self ._rows = temp_mat._rows[:]
         return self

from matrix import Matrix

if __name__ == "__main__":
    m1= Matrix(3,3,0)
    
    for value in m1:
        print(value)

    m1[0][0]=35
    
    m2 = Matrix(3, 3,11)
    print(m1)
    print(m2)
    print(m1 + m2)
    print(m1 - m2)
    
    m2 += m2
    m2[2][1] = 3
    print(m2)
    m2.transpose()
    print(m2)
    print((m2 == m1))
    print(m2.get_rank())
'''
