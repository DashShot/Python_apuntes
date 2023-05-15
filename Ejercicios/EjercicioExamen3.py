'''Desarrollar un programa en Python que reciba como argumento la
ruta de un fichero y muestre por pantalla sus últimas 10 líneas. Opcionalmente
el programa podrá recibir un segundo parámetro que indique el número de
líneas que se desean mostrar desde el final del fichero. A continuación, se
muestra dos ejemplos de llamadas que el programa deberá soportar:
○ python tail.py --file=/etc/hosts
○ python tail.py --file=/etc/hosts --lines=25
Nota: el programa debe respetar el formato de llamada proporcionado
'''

import sys

#Comprobamos la llamada
if len(sys.argv) > 3:
    sys.exit("Demasiados argumentos, La forma de ejecutar ha de ser --file=  --lines: o --file \n")
elif len(sys.argv) < 2:
    sys.exit("Faltan argumentos, La forma de ejecutar ha de ser --file=  --lines: o --file \n")

    