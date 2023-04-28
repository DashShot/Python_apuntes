"""
● Añadir a la clase Matrix la posibilidad de crear matrices de ceros, matrices
identidad y matrices con valores aleatorios
○ utilizar static factory methods
"""
import random


class Matrix:

    def __init__(self, m, n, value=0):
        self.m = m
        self.n = n
        self._rows = [[value] * n for _ in range(m)]

    def __getitem__(self, idx):
        return self._rows[idx]

    def __setitem__(self, idx, item):
        self._rows[idx] = item

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self._rows])
        return s + '\n'

    def transpose(self):
        self.m, self.n = self.n, self.m
        self._rows = [list(item) for item in zip(*self._rows)]

    def get_rank(self):
        return self.m, self.n

    def __eq__(self, mat):
        return mat._rows == self._rows

    def __add__(self, mat):
        if self.get_rank() != mat.get_rank():
            raise Exception("Trying to add matrixes of varying rank!")
        ret = Matrix(self.m, self.n)
        for x in range(self.m):
            row = [sum(item) for item in zip(self._rows[x], mat[x])]
            ret[x] = row
            return ret

    def __sub__(self, mat):
        if self.get_rank() != mat.get_rank():
            raise Exception("Trying to add matrixes of varying rank!")
        ret = Matrix(self.m, self.n)
        for x in range(self.m):
            row = [item[0] - item[1] for item in zip(self._rows[x], mat[x])]
            ret[x] = row
            return ret

    def __iadd__(self, mat):
        temp_mat = self + mat
        self._rows = temp_mat._rows[:]
        return self

    def __isub__(self, mat):
        temp_mat = self - mat
        self._rows = temp_mat._rows[:]
        return self

    @classmethod
    def make_random(cls, m, n, low=0, high=10):
        mat = cls(m, n)
        for index, row in enumerate(mat):
            mat[index] = [random.randrange(low, high) for _ in range(mat.n)]

        return mat

    @classmethod
    def make_zero(cls, m, n):
        mat = cls(m, n, 0)
        return mat


if __name__ == "__main__":
    m1 = Matrix(3, 3, 0)

    for value in m1:
        print(value)

    m1[0][0] = 35

    m2 = Matrix(3, 3, 11)
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
