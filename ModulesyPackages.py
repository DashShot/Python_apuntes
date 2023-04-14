
print("Archivo con información sobre Módulos y paquetes en python")

''' ----------------------------------------------------------------------------
                    [ MODULOS Y PAQUETES ]
            
- Todo fichero en python .py es un módulo
    - Otros ficheros pueden acceder a sus funcionalidades importándolo

EJEM:
def fib(n): # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

def main():
    import sys
    fib(int(sys.argv[1])

if __name__ == "__main__":
    main()
-----------
import fibo

fibo.fib(100)
fib_serie = fibo.fib2(10)
----------------------------------

- Consultar las 
'''