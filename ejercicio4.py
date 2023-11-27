'''
4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
'''
nombre = input ('Ingrese su nombre: ')
letra = input(f'Hola, {nombre}, por favor ingrese la letra de la cual quire saber si es una vocal o no: ')

def esVocal(letra):
    vocales = ["a", "e", "i", "o", "u"]
    if letra in vocales:
        return True
    else:
        return False

print ( f'La letra {letra}, es una vocal: {esVocal(letra)}' )