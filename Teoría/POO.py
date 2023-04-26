
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

'''
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
