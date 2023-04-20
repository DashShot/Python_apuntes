
print("Archivo con información sobre conjuntos")

'''--------------------------------------------------------------------

            [ CONJUNTOS ]

- Construcción: llaves, compresión y constructores

EJEM:
# Braces
empty_set = {}
lottery_numbers = {1, 34, 38, 43, 53}
user_names = {"juan.perez", "antonio.garcia", "luis.lopez"}

# Set comprehension
vowels_removed = {c for c in "Learning Python" if c not in "aeiouAEIOU"}
bus_lane_penalties = ["32233-GXP", "1323-DGL", "09877-GRU", "77776-LKP", "09877-GRU", "44555-PTX"]
allowed_vehicles = {"32233-GXP", "965484-KJL", "09877-GRU"}
unique_plates = {licence_plate for licence_plate in bus_lane_penalties
 if licence_plate not in allowed_vehicles}

#Constructors
empty_set = set()
lottery_numbers = set([1, 34, 38, 43, 53])
different_characters = set("Learning Python")
number_to_choose_from = set(range(9))
unique_plates = set(bus_lane_penalties).difference(allowed_vehicles)

-----------------------

- Conjuntos inmutables: frozenset

stop_words = frozenset(
 ["a", "about", "after", "all", "also", "always", "am", "an", "and", "any", "are", "at", "be", "been", "being",
 "but", "by", "came", "can", "cant", "come", "could", "did", "didnt", "do", "does", "doesnt", "doing", "dont",
 "else", "for", "from", "get", "give", "goes", "going", "had", "happen", "has", "have", "having", "how", "i", "if",
 "ill", "im", "in", "into", "is", "isnt", "it", "its", "ive", "just", "keep", "let", "like", "made", "make", "many",
 "may", "me", "mean", "more", "most", "much", "no", "not", "now", "of", "only", "or", "our", "really", "say", "see",
 "some", "something", "take", "tell", "than", "that", "the", "their", "them", "then", "there", "they", "thing",
 "this", "to", "try", "up", "us", "use", "used", "uses", "very", "want", "was", "way", "we", "what", "when",
 "where", "which", "who", "why", "will", "with", "without", "wont", "you", "your", "youre"])

- Operaciones soportadas por set y forzenset
    https://docs.python.org/3.9/library/stdtypes.html#set-types-set-frozenset

------------------------------------

EJER:
● Coge un texto de wikipedia
● Copialo en una cadena de caracteres de python
● Desarrolla un pequeño script que calcule el número de palabras diferentes que
contiene
    ○   elimina previamente las stop words
● Muestra por pantalla las palabras distintas
● Muestra por pantalla el número total de palabras 

SOL:


-------------------------------------



'''