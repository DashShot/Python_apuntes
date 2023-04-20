
print("Archivo con información sobre las declaraciones de funciones en python")

''' ----------------------------------------------------------------------------
                    [ DECLARACIÓN DE FUNCIONES ]

Las funciones son objetos

- Palabra reservada def
    def -> crea un objeto función y le asigna un nombre

def function_name (arg1, arg2,..., argN):
 statements
 return value

EJEM:
def times (x, y):
    return x*y
 
def sum_range (first, last):
     total = 0
     i=first
     while i<=last:
        total=total+i
        i+=1
    return total
--------------------------
EJER:
Desarrollar una función que permita calcular la intersección de dos secuencias
    ○ ¿qué tipo de secuencias?
        ■ cualquiera: cadenas de texto, listas, tuplas...
SOL:

--------------------------------------

- Paso de argumentos -> Por asignación
    A los parámetros formales se les asigna el valor de ls parámetros reales
        - Asignación /= copia
        - Los parámetros formales son referencias a los objetos pasados en la llamada
     
EJEM:
def changer (a,b):
     a=2
     b[0]='spam'
     
x=1
l=[1,2]
changer(x,l)
print(x, l) #???
------------
def to_lower(text):
     text = text.lower()
     print(text)
my_text="HOLA"
to_lower(my_text)
print(my_text) #????
---------------

- Asignación de parámetros
    + Por defecto la asignación es por posición
    + se pueden usar keywords

EJEM:
def volume3D (width, height, depth):
     print (f"Volume size:{width, height, depth}")
     ...
     
volume3D (128, 64, 32)
volume3D (depth=64, width=128, height=64)
volume3D (128, depth=64, height=64)
volume3D (32, width=128, height=64)
# TypeError: volume3D() got multiple values for
argument 'width'
------------------

- Número de argumentos arbitrarios
    + *args, **kwargs

EJEM:
def foo(a, *args, **kwargs):
     print(a)
         for arg in args:
         print(arg)
     
     for key, value in kwargs.items():
         print(key, value)
 
foo(1, 2, 3, x=1, y=2)
-------------------------

EJER:
Desarrollar una función que permita calcular la intersección de dos secuencias
    ○   dos, tres, cuatro, cinco … n secuencias

SOL:

-------------------------

- Las funciones tambien se pueden pasar como argumento
    + En python las funciones son objetos

EJEM:
def reduce(function, *args):
     result = args[0]
     for arg in args[1:]:
        if function(arg, result):
            result = arg
    return result
    
def less_than(x, y):
    return x < y

def grtr_than(x, y):
    return x > y

print(reduce(less_than, 4, 2, 1, 5, 6, 3))
print(reduce(grtr_than, 4, 2, 1, 5, 6, 3))

----------------------------
'''