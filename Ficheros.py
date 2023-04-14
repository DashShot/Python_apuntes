import operator

print("Archivo con información sobre el manejo de ficheros en python")

''' ----------------------------------------------------------------------------
                    [ FICHEROS ]

- Operaciones comunes

EJEM:
file = open("./resources/fb.csv")
file = open("./resources/fb.csv", "r")
file = open("./resources/fb.csv", "w")
file = open("./resources/fb.csv","a")
file = open("./resources/fb.csv", "r+")
file = open("./resources/data.bin", "rb")
file = open("./resources/fb.csv", encoding='latin-1')

text=file.read() # read entire file into a single string
first_houndred = file.read(100) # read up to next 100 characters (or bytes) into a string
first_line=file.readline() # read next line into a string

all_lines = file.readlines() # Read entire file into list of line strings
for line in file: # File iterators read line by line
    print(line)

file.write(a_string) # Write a string of characters (or bytes) into file
file.write_lines(a_list) # Write all line strings in a list into file

file.close()
file.flush() # Flush output buffer to disk without closing
file.seek(N)
-------------

- Forma correcta de abrir ficheros

EJEM:
with open("./resources/FB.csv") as file:
    facebook_stocks = file.read()
query_name = "Close"
column_names = facebook_stocks.splitlines()[0].split(',')

close_index = column_names.index(query_name)
step = len(column_names)
begin = close_index + step

split_text = facebook_stocks.replace("\n", ",").split(',')
close_values = split_text[begin::step]

max_value = max(map(float, close_values))
print(max_value)

EJEM2:
VALUE = 200
FIELD = "Close"

new_file_lines = []

with open("./resources/FB.csv") as file:
 header_line = file.readline()
 new_file_lines.append(header_line)
 
 index = header_line.split(',').index(FIELD)
 for line in file:
    close_value = float(line.split(',')[index])
    if close_value > VALUE:
        new_file_lines.append(line)

with open("./resources/FB_filtered.csv", "w") as file:
    file.writelines(new_file_lines)

-------------------------

- pickle -> forma de serializar (NO ES SEGURO)
    +no es posible conozer lo que desserializas (puerta entrada vulnerabilidades)
    + Usar JSON resistido por python
    
EJEM:
import pickle
stop_words = frozenset(
 ["a", "about", "after", "all", "also", "always", "am", "an", "and", "any", "are", "at", "be", "been", "being",
 "but", "by", "came", "can", "cant", "come", "could", "did", "didnt", "do", "does", "doesnt", "doing", "dont",
 "else", "for", "from", "get", "give", "goes", "going", "had", "happen", "has", "have", "having", "how", "i", "if",
 "ill", "im", "in", "into", "is", "isnt", "it", "its", "ive", "just", "keep", "let", "like", "made", "make", "many",
 "may", "me", "mean", "more", "most", "much", "no", "not", "now", "of", "only", "or", "our", "really", "say", "see",
 "some", "something", "take", "tell", "than", "that", "the", "their", "them", "then", "there", "they", "thing",
 "this", "to", "try", "up", "us", "use", "used", "uses", "very", "want", "was", "way", "we", "what", "when",
 "where", "which", "who", "why", "will", "with", "without", "wont", "you", "your", "youre"])

with open('datafile.pkl', 'wb') as file:
    pickle.dump(stop_words, file)
------------------------

EJER:
Escribe un programa en python que ordene por popularidad las shells usadas en
un equipo Linux
    + analizar el fichero /etc/passwd
SOL:
BASH_POSITION = 6
new_file_lines = []
shells = {}

with open("./Resources/passwd") as file:
    for line in file:
        shell = line.strip().split(":")[BASH_POSITION]
        if shell:
            shells[shell] = shells.get(shell,0)+1

    ordered_shells2 = sorted(shells.items(), key=operator.itemgetter(1),reverse=True)
    ordered_shells = sorted(shells, key=shells.get, reverse=True)
    print(ordered_shells)
    print(ordered_shells2)

    new_file_lines=''.join(map(ordered_shells2)) AJUSTAR CREAR FICH

with open('./Resources/shellOrden.txt','w') as file:
    file.write(new_file_lines)
--------------------------------------------------------


'''