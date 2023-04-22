
print("Archivo con información sobre los distintos tipos de datos en python")

''' ----------------------------------------------------------------------------
                    [ BOOLEANOS ]

file_exists = False
connection_failed = True
finished = True
print(id(file_exists))
print(id(connection_failed))
print(id(finished))

print (file_exists==connection_failed)
print (connection_failed==finished)

print (file_exists is connection_failed)
print (connection_failed is finished)

connection_failed = not connection_failed
print (connection_failed is finished)

------------------------------------------------------------------------------------------
                    [ NUMÉRICOS ]

import math
import random

value1 = random.randrange(1, 100)
value2 = random.randrange(1, 100)

print(f"{value1} * {value2} = {value1*value2}")
value1 = random.uniform(1.0, 100.0)
value2 = random.uniform(1.0, 100.0)
result = value1+value2

print(f"{value1} + {value2} = {result} (rounded: {math.ceil(result)})")
#print(f"{value1:.2f} + {value2:.2f} = {result:.2f} (rounded: {math.ceil(result)})")

--------------------------------------------------------------------------------------------
                    [ TEXTO ]

# Texto
error_message = "NameError: name 'a' is not defined."
start = 11
stop = 15

print(error_message[start:stop]) # portion from index 11 to 15
print(error_message[start:]) # portion from 11 till last element
print(error_message[:stop]) # portion from index 0 to 15
print(error_message[:]) # all items

step=2
print(error_message[start:stop:step]) # portion from 11 till 15 with increment of 2







'''