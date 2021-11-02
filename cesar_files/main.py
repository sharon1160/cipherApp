from cesar import *
from preprocess import funcion2, funcion4
import os

#directorio_salida = r'C:\Users\BRAYAN LIPE\Documents\UNSA\2021\SEMESTRE B\Seguridad en computacion\Teoría\Unidad 2\tarea 2\code'
#files = os.listdir(directorio_salida)
sign_list = [' ', '.', ',', ';', '¡', '!', '¿', '?', '\n']
accent_list = ['á', 'é', 'í', 'ó', 'ú']


def menu(text):
    print("Para cifrar un texto pulse [1] o para descifrar [2]\n")
    mode = int(input('Opcion: '))
    if mode is 1:
        print("*******Cifrado******\n")
        k = int(input('Clave numérica: '))
        preprocess_text = funcion2(text, accent_list)
        print(preprocess_text,'\n----------------------------------------')
        preprocess2_text = funcion4(preprocess_text, sign_list)
        print(preprocess2_text,'\n----------------------------------------')
        ciphered_text = cesar_cifrar(preprocess2_text, k)
        print(ciphered_text,'\n----------------------------------------')
        f = open("cifrado.txt", "w+")
        f.write(ciphered_text)
        f.close()
    if mode is 2:
        print("*******Descifrado******\n")
        key = int(input('Clave numérica: '))
        file = open("cifrado.txt", 'r', encoding = 'utf-8').read()
        text = cesar_descifrar(file, key)
        print(text,'\n---------------------------------------')
                

def main():
    print("******Bienvenido al Cifrado/Descifrado de Cesar*********\n")
    print("¿Como desea ingresar el texto?: \n")
    print("Presione 0 para ingreso por teclado\n")
    print("Presione 1 para ingreso por archivo\n")
    opcion = int(input('Opción: '))
    
    if opcion == 0:
        c = str(input('Escriba el texto a cifrar: '))
        menu(c)
    elif opcion == 1:
        filename = str(input('Nombre del archivo: '))
        file = open(filename, 'r', encoding = 'utf-8').read()
        menu(file)
    else:
        print("\nError!, seleccionó una opcion incorrecta\n")
        print("Intente de nuevo\n")
        main()


if __name__ == '__main__':
    main()