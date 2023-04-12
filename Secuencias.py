
print("Archivo Con información sobre secuencias")

''' -----------------------------------------------------------------------
                [ LISTAS ]
        
        - COMPRESIÓN DE LISTAS
        
-EJEM1:  
squares=[]
for x in range(10):
    squares.append(x**2)
print (squares)
--------------------------------
squares = [x**2 for x in range(10)]
print(squares)

-EJEM2:
some_numbers = [-4, -2, 0, 2, 4]
dp_numbers=[]
for number in some_numbers:
    if number>=0:
    dp_numbers.append(number * 2)
print(dp_numbers)
-------------------------------------------
numbers = [-4, -2, 0, 2, 4]
dp_numbers = [number*2 for number in numbers if number >= 0]
print(dp_numbers)

-EJEM3:
combinations = []
for x in [1,2,3]:
 for y in [3,1,4]:
    if x != y:
        combinations.append([x, y])
print(combinations)
#-------------------------------------------
combinations = [[x, y] for x in [1,2,3] for y in [3,1,4] if x != y]
print(combinations)

-EJEM4:
matrix = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
transposed = []
for i in range(5):
    transposed.append([row[i] for row in matrix])
print(transposed)
#------------------------------------------
transposed = [[row[i] for row in matrix] for i in range(5)]
print(transposed)
#-------------------------------------------
print(list(zip(*matrix)))

    - PILAS -> append y pop

undo_history = []
undo_history.append("pwd")
undo_history.append("ls")
undo_history.append("cd ~/development/LP/")
undo_history.append("mkdir examples")
print("Operations so far:")
print("\n".join(undo_history))

print("------------------------------")
print("Undoing last two operations...")
print("------------------------------")

undo_history.pop()
undo_history.pop()
print("Operations so far:")
print("\n".join(undo_history))


    - COLAS -> Se pueden hacer con listas pero NO SE DEBE(mucho coste)
            -> Usar collections.deque
            
from collections import deque
import time
jobs_queue = deque([])
jobs_queue.append("[Job 233] Train NN for image classification. TFG 123.")
jobs_queue.append("[Job 234] Test NN. TFG 431.")
jobs_queue.append("[Job 235] Train NN for language traslation. TFG 431.")
print(jobs_queue)
time.sleep(5) # [simulation] execution time for Job 233
jobs_queue.popleft()
print(jobs_queue)
time.sleep(2) # [simulation] execution time for Job 233
jobs_queue.popleft()
print(jobs_queue)
--------------------------------------------------------------------------------------------
               [ TUPLAS ]
                
- Secuencias inmutables
empty_tupple = ()
singleton_tuple = (54,)
return_value = (5, x, "Good quality")
resolution = (1920, 1080)
matrix_coordinates = (3, 4)
- Operaciones
    collections.abc.Sequence 
    https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
-Tuple Packing/Unpacking
volume_size = 256, 128, 64
print(f"Volume size: {volume_size}")

width, height, depth = volume_size
print(f"Volume width={width}, volume height={height}, volume depth={depth}")

- EJERCICIO:
Dada una secuencia de datos en python (lista, tupla, cadena de caracteres). Utilizar
compresión de listas para convertir esa secuencia en una lista de tuplas, donde el
primer elemento de las tuplas será un índice en la colección y el segundo será su
valor. Ejemplos:
["examen", "de", "python"] - > [(1,"examen"), (2,"de"), (3,"python")]
("examen", "de", "python") - > [(1,"examen"), (2,"de"), (3,"python")]

seq = ["examen", "de", "python"] 

seq_result = [(i+1,seq[i]) for i in range(len(seq)]
print(seq)

-------------------------------------------------------------------------------------------------

                    [ RANGOS ]
                    
- Secuencias inmutables de números enteros          
        Comunmense se utilizan para iterar (for)
- Constructores
    range (stop)
    range (start, stop, [step])

EJEM:
indexes = range(10)
print(f"Range: {indexes}, list from range: {list(indexes)}") #?????

indexes = range(1,11)
print(f"Range: {indexes}, list from range: {list(indexes)}") #?????

odds = range(1,20,2)
print(f"Range: {odds}, list from range: {list(odds)}") #?????

evens = range(0,32,2)
print(f"Range: {evens}, list from range: {list(evens)}") #?????

negative_range = range(0,-100,-25)
print(f"Range: {negative_range}, list from range: {list(negative_range)}") #?????

empty_range = range(0)
print(f"Range: {empty_range}, list from range: {list(empty_range)}") #?????

empty_range = range(1, 0)
print(f"Range: {empty_range}, list from range: {list(empty_range)}") #?????
--------------------------------

- Operaciones:
    (collections.abc.Sequence)

EJEM2:
evens_through_20 = range(0, 20, 2)

11 in evens_through_20 # False
10 in evens_through_20 # True

evens_through_20.index(10) # 5
evens_through_20[5] # 10
evens_through_20[:5] # range (0,10,2)
evens_through_20[-1] # 18
------------------------------
- Rangos flotantes:
    float_range = [i/10 for i in range (0,10,1)]
    
'''



