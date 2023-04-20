
print("Archivo con información sobre las Instrucciones de control y la función ZIP en python")

'''---------------------------------------------------------------------------

            [ INSTRUCCIONES DE CONTROL ]

--- if ----

if cont<0:
 print ('No occurrences were found')

if "ERROR" in jenkins_message:
    print("Oh no!")

if word in stop_words:
    stop_words_count += 1

----- if else -------

if "Kylian Mbappe" not in goals_by_player:
    goals_by_player["Kylian Mbappe"] = 1
else:
    goals_by_player["Kylian Mbappe"] += 1

x = int(input("Enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

---- while ------

while i <= n:
    sum = sum + i
    i = i+1

---- for -------

for i in range(10):
     print(i)

for i in range(1, 10):
    print(i)
 
for i in range(1, 10, 2):
    print(i)

for i in reversed(range(1, 10, 2)):
    print(i)
    # for i in range(9, 0, -2):

for stop_word in stop_words:
    print (stop_word)

for index, stop_word in enumerate(stop_words):
    print (index, stop_word)

for stop_word in sorted(stop_words):
 print (stop_word)


EJEM:
goals_by_player = {"Erling Haaland": 27, "Leo Messi": 29, "Cristiano Ronaldo": 31,
    "Robert Lewandowski": 45, "Kylian Mbappe": 20}

for key in goals_by_player:
    print(key)

for key in goals_by_player.keys():
    print(key)

for value in goals_by_player.values():
    print(value)

for key,value in goals_by_player.items():
    print(key, value)

------------------------------------------------------------------------------------------

                            [ ZIP ]

- La función genera un iterador de tuplas a partir de varias colecciones

EJEM:
spanish = ['uno', 'dos', 'tres']
english = ['one', 'two', 'three']
french = ['une', 'deux', 'trois']
zipped = zip(spanish, english, french)
print(list(zipped))# [('uno', 'one', 'une'), ('dos', 'two', 'deux'), ('tres', 'three', 'trois')]



               
'''