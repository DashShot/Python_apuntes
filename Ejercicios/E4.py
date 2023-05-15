def pig_latin(phrase):
    vocales = ['a', 'e', 'i', 'o', 'u']
    if phrase[0].lower() in vocales:
        return phrase+"way"
    else:
        return phrase[1:] + phrase[0]+"ay"


phrase1 = "air"
phrase2 = "python"

print(pig_latin(phrase1))
print(pig_latin(phrase2))