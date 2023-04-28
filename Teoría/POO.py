
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

'''