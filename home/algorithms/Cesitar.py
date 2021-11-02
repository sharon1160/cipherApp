import string

#alfabeto = list(string.ascii_lowercase + string.ascii_uppercase)
alfabeto = list(string.ascii_uppercase)
#alfabeto = list(string.ascii_lowercase)

def cesar_cifrar(text, key):
    cipher = ""
    for i in range(len(text)): 
        char = text[i]
        if (char.islower()):
            cipher += chr((ord(char) + key - 97) % 26 + 97) 
        else:
            cipher += chr((ord(char) + key - 65) % 26 + 65) 
    return cipher
    '''text = text.upper()
    coded_text = ''
    for letra in text:
        if letra in alfabeto:
            indice_actual = alfabeto.index(letra)
            indice_cesar = indice_actual + key

            if indice_cesar>27:
                indice_cesar -= 27
            print(indice_cesar)
            coded_text += alfabeto[indice_cesar]
        else:
            coded_text += letra
    
    return coded_text'''

def cesar_descifrar(text, key):
    plain = ""
    for i in range(len(text)):
        char = text[i]
        if (char.islower()):
            plain += chr((ord(char) -97-key) % 26 + 97)
        else:
            plain += chr((ord(char) -65-key) % 26 + 65)
    return plain
    '''decoded_text = ''
    for letra in text:
        if letra in alfabeto:
            indice_cesar = alfabeto.index(letra)
            indice_original = indice_cesar - key

            if indice_original<0:
                indice_original += 27

            decoded_text += alfabeto[indice_original]
        else:
            decoded_text += letra
    
    return decoded_text'''

def brute_force(text):
    for i in range(26):
        print(i, ":: "+chr(65+i)+": "+ cesar_descifrar(text,i))
    '''for key in range(len(alfabeto)):
        translated = ''
        for symbol in text:
            if symbol in alfabeto:
                num = alfabeto.index(symbol)
                num = num - key
            if num < 0:
                num = num + len(alfabeto)
            translated = translated + alfabeto[num]
        else:
            translated = translated + symbol
        print('Hacking key #%s: %s' % (key, translated))'''
    
'''message = "Bota tu gaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaas chupetin pipipipipipipipipii la recoooonn"
m_c = cesar_cifrar(message, 50)
print(m_c)
#print(cesar_descifrar(message, 3))
brute_force(m_c)'''
