'''
6 - Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
'''
nombre = input ('Ingrese su nombre: ')

def invertir_cadena(cadena):
    cadena_invertida = ""
    for caracter in cadena[::-1]:
        cadena_invertida += caracter
    return cadena_invertida

cadena = input(f" {nombre} Ingrese una cadena de texto: ")
print( 'El texto de la palabra invertida es el siguiente: ', invertir_cadena(cadena))