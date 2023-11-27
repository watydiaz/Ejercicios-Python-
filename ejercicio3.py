'''
3 - Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
'''
palabra = input('Ingrese una palabra: ')
def contarLetras(palabra):
    contar = len(palabra)
    return contar

resultado = contarLetras(palabra)
print (f'La cantidad de letras que tiene la palabra {palabra}, es de: {resultado}, caracteres o letras.')