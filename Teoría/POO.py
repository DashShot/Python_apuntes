
'''
----------------------------------------------------------------------------------
                            [ POO ]

- No existen atributos/métodos privados
    - si comienzan con _ se consideran parte "no pública"
        Ya conocidos
    - Se usan estrategias de renombrado para tratar de evitar usos incorrectos

- Self (this)

- Operadores https://python-course.eu/oop/magic-methods.php
- Metdos especiales https://docs.python.org/3/reference/datamodel.html#specialnames
EJEM:
 def __str__(self): -> (ToString) genera cadcaracteres
    return f"({self.x},{self.y})"

 def __repr__(self): # used by repr -> codigo para crear otro objeto igual
    return f"Point2D({self.x},{self.y})"

EJEM:
class Point2d:

 def __init__(self, x=0, y=0):
    self._x = x
    self._y = y
 def __str__(self):
    return f"({self._x},{self._y})"

 def __repr__(self): # used by repr
    return f"Point2D({self._x},{self._y})"

 def getx(self):
    return self._x

 def gety(self):
    return self._y

 def shift(self, x_offset, y_offset):
    self._x += x_offset
    self._y += y_offset

if __name__ == "__main__":
    point = Point2d( 0, 0)
    print(point)
    point.shift( 3, 4)
    print(point)
    print(repr(point))
    print(point.x)

    point_ints = Point2d(0, 0)
    point_floats = Point2d(0., 0.)
    point_strings = Point2d("0.", "0.")
    point_lists = Point2d([0, 1, 2], [3, 4, 5])

    point_ints.shift(3, 4)
    print(point_ints)
    point_floats.shift(3, 4)
    print(point_floats)
    point_strings.shift("3", "4")
    print(point_strings)
    point_lists.shift([6], [7])
    print(point_lists)

--------------------------------------------------------------------------------------------

- Operador __call__

    - es llamado cuando una instancia es llamada
    - Permite a una instancia actuar como función

    - Caso de uso -> decoradores
EJEM:
class Prod:
    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        return self.value * other

x = Prod(2)
x(3) #HACE LO DEFINIDO EN CALL
x(4)
-------------------------------------------------
class Memoize:
    def __init__(self, func):
        self.func = func
        self.history = {} #DICCIONARIO PARA ALMACENAR VALORES

    def __call__(self, *args):
        if args not in self.history:
            self.history[args] = self.func(*args)
        return self.history[args]

@Memoize # -> fibonacci = Memoize(fibonacci) #Cambias la llamda a la función por una llamada al constructor para ver el call
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) #se vuelve a llamar a call

print(fibonacci(2))
print(fibonacci(2))

---------------------------------------------------------------

- Atributos Estáticos

    -@staticmethod

Ejemplo
class UrjcStudent:
    common_id = 'urjc-s' # static attribute(class variable)

    def __init__(self, name):
        self.name = name


a = UrjcStudent('Jose Perez')
b = UrjcStudent('Antonio Garcia')

print("-----------------")
print(a.common_id) #urjc-s
print(b.common_id) #urjc-s
print(UrjcStudent.common_id) #RECOMENDADO urjc-s
a.common_id = 'URJC-S'
print("-----------------")
print(a.common_id) #URJC-S
print(b.common_id) #urjc-s
print(UrjcStudent.common_id) #urjc-s

UrjcStudent.common_id = 'US'
print("-----------------")
print(a.common_id) #URJC-S
print(b.common_id) #US
print(UrjcStudent.common_id) #US
----------------------------------------------------------------
    @staticmethod #FORMA CORRECTA
    def is_full_name(name):
        return len(name.split(" "))>1

student_name = "Antonio Perez"
if UrjcStudent.is_full_name(student_name):
    student = UrjcStudent(student_name)
--------------------------------------------------------
    @classmethod # METODO ESTATICO FACTORIA (STATIC FACTORY METHOD)
    def from_string(cls, name): #CLS -> Hace referencia a la clase desde la que se invoca /MUY UTIL PARA HERENCIA
        if not UrjcStudent.is_full_name(name):
            return None
        s = name.split(" ")
        return cls(s[0], s[1])
---------------------------------------------------------------
- Sobrecarga de métodos
    - parámetros por defecto
    - args, kwargs
    - un nombre para cada cosa
    - decoradores
------------------------------------------------------------------
- Decorador @property / @atrb.setter
                (getter)

    - aumentar legibilidad y mantener encapsulación

class Complex:

    def __init__(self, real, img):
        self._parts = [real, img]

    def __str__(self):
        if self.img<0:
            return f"{self.real}{self.img}i"
        return f"{self.real}+{self.img}i"

    @property
    def real(self):
        return self._parts[0]

    @real.setter
    def real(self, value):
        self._parts[0] = value

    @property
    def img(self):
        return self._parts[1]

    @img.setter
    def img(self, value):
        self._parts[1] = value

if __name__== "__main__" :
    c = Complex ( 1, -1)
    c.real= 4
    c.img=5
    print(c.real, c.img)
--------------------------------------------------------

- Herencia

    - resolución de nombres (atributos/métodos) MRO
        -Orden:
            - Busqueda de abajo-arriba por la jerarquía de la herencia
            - Si herencia multiple -> abajo-arriba y izquierda-derecha

class Person:
    def __init__ (self, name, job= None, pay=0):
        self._name = name
        self._job = job
        self._pay = pay

    def lastname (self):
        return self._name.split()[- 1]

    def giveraise (self, percent):
        self._pay = int(self._pay * ( 1 + percent))

    def __str__(self):
        return f'[Person: {self._name}, {self._pay}]'

class Manager(Person):
    def __init__ (self, name, pay):
    # Person.__init__(self, name, 'mgr', pay)
        super().__init__ (name, 'mgr', pay)

    def giveraise (self, percent, bonus= .10):
        super().giveraise(percent + bonus)

if __name__ == '__main__':
    bob = Person( 'Bob Smith')
    sue = Person( 'Sue Jones', job='dev', pay=100000)
    tom = Manager( 'Tom Jones', 50000)
    employees = [bob, sue, tom]

    for employee in employees:
        employee.giveraise( 10)
    print(employee)

-------------------
-Resolución de nombres MRO
class A: pass
class B: pass
class C: pass
class D: pass
class E: pass
class K1(C, A, B): pass
class K3(A, D): pass
class K2(B, D, E): pass
class Z(K1, K3, K2): pass
print(Z.mro())
# [Z, K1, C, K3, A, K2, B, D, E, O]

---------------------------------
- Classes abstractas

from abc import ABC, abstractmethod

class Processor(ABC):
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        for line in self.reader:
            processed_line = self.converter(line)
            self.writer.write(processed_line)

    @abstractmethod
    def converter(self, data):
    pass

class Uppercase(Processor):
    def converter(self, data):
    return data.upper()

class HTMLize:
    def write(self, line):
    print(f"<PRE>{line.rstrip()}</PRE>")

import sys
if __name__ == '__main__':
    obj = Uppercase(open('./ElhPolar_esV1.lex'), HTMLize())
    obj.process()

Duck typing: “si se comporta como un pato, es un pato”

'''