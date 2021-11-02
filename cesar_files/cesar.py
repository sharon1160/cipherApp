import string

alfabeto = list(string.ascii_lowercase + string.ascii_uppercase)


def cesar_cifrar(text, key):
    coded_text = ''
    for letra in text:
        if letra in alfabeto:
            indice_actual = alfabeto.index(letra)
            indice_cesar = indice_actual + key

            if indice_cesar>42:
                indice_cesar -= 42
            coded_text += alfabeto[indice_cesar]
        else:
            coded_text += letra
    
    return coded_text


def cesar_descifrar(text, key):
    decoded_text = ''
    for letra in text:
        if letra in alfabeto:
            indice_cesar = alfabeto.index(letra)
            indice_original = indice_cesar - key

            if indice_original<0:
                indice_original += 42

            decoded_text += alfabeto[indice_original]
        else:
            decoded_text += letra
    
    return decoded_text

