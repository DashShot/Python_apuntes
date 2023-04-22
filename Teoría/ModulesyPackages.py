
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

- Librería estándar:

módulo zipfile

python -m zipfile -c code.zip ./lp/code/
python -m zipfile -l code.zip

EJEM: (Correo desde python)
import smtplib, ssl

port = 465 # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "raul.cabido@gmail.com"
receiver_email = "raul.cabido@urjc.es"
password = input("Password: ")
message = """\
Subject: Learning Python

Message sent from Python script."""

#Creates a secure connection with Gmail’s SMTP server
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

-------------------------------
 - Muchas posibilidades al buscar información

EJER:
Programa que muestre el estado de las acciones de facebook los últimos 30 días
○ módulo datetime

Programa que reciba como argumento una fecha de inicio o otra de fin y
muestre el estado de las acciones en ese rango. Si no se proporciona fecha de fin
tomar el día actual.
○ módulo argparse


------------------------------------------------------------------------------

                            [ PAQUETES ]

- Son un directorio que contiene distintos módulos

- el fichero _init.py era necesario para tratar estos directorio como paquetes (hasta python 3.3)

        -¿poruqe?

- import -> importa funcionalidades
    para importar todas:
        form package import __all__


--------------------------------------------------------------------------------

                            [ PyPI ]

- Repositorio de paquetes de terceros

pip install packagename
pip install packagename==version
pip install --upgrade packagename
pip uninstall packagename

- Es inmpartante un gestor de dependencias para resolver problemas entre distintos paquetes
 
'''