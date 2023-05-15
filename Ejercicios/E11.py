def longest_word(cad):
    max_count = 0
    max_word = ""
    for word in cad.split():
        num_letras = {}
        for letra in word:
            letra = letra.lower()
            num_letras[letra] = num_letras.get(letra, 0) +1
        word_cont = max(num_letras.values())
        if word_cont > max_count:
            max_word = word
            max_count = word_cont

    return max_word

print(longest_word("cual de estas es la palabra más larga esternocleidomaestoideo"))