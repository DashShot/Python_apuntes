
print("Archivo que contiene información sobre mapas")

'''------------------------------------------------------------------

                            [ MAPAS ]

- Estructura de datos que asocia o mapea claves con valores

    - no permite claves repetidas
    - varias claves pueden estar asociadas al mismo valor
    - la búsqueda de un valor asociado a una clave es muy eficiente (Con una tabla hash O(1))
    
- Construcción: llaves, compresión y constructores

EJEM:
# Braces
empty_dict = {}
goals_by_player = {"Erling Haaland": 27, "Leo Messi": 29, "Cristiano Ronaldo": 31,
 "Robert Lewandowski": 45, "Kylian Mbappe": 20}
 
# Dict comprehension
pow_cache = {x: x ** 2 for x in range(25)}
goals = {value: key for key, value in goals_by_player.items()}
# goals = {value:[key] for key, value in goals_by_player.items()}

# Constructors
empty_dict = dict()
color_code = dict([('RED', 100), ('GREEN', 200), ('BLUE', 110)])
urjc_world_coordinates = dict(lat=40.335913308819116, lon=-3.8732171058654785)

---------------------------------

- Operaciones soportadas
    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

EJEM2:
goals_by_player = {"Erling Haaland": 27, "Leo Messi": 29, "Cristiano Ronaldo": 31,
    "Robert Lewandowski": 45, "Kylian Mbappe": 20}

players = goals_by_player.keys()
goals_in_total = sum(goals_by_player.values())
print(f"{goals_in_total} goals between:{list(players)}")
# print (f"{goals_in_total} goals between:{list(goals_by_player)}")
# print (f"{goals_in_total} goals between:{players}")

goals_by_player["Neymar Jr."] = 13
goals_by_player["Erling Haaland"] += 1
del goals_by_player["Neymar Jr."]
print(f"Statistics: {goals_by_player}")

------------------------------------

EJER:
● Coge un texto de wikipedia
● Copialo en una cadena de caracteres de python
● Desarrolla un pequeño script que calcule el número de palabras diferentes que
contiene
    ○ elimina previamente las stop words
● Muestra por pantalla las palabras distintas
● Muestra por pantalla el número total de palabras
● Calcula el número de veces que aparece cada palabra distinta y muéstralo
● Calcula también la frecuencia de aparición de cada stop word (en %) con
respecto al total de palabras

SOL:

'''

