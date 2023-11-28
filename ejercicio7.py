'''
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.
'''
nombre = input ('Ingrese su nombre: ')
cadena = input ('Ingrese la palabra que quiere verificar: ')

def es_palindromo(cadena):
    cadena = cadena.lower()
    palabra_invertida = cadena[::-1]
    return cadena == palabra_invertida

print (f'la palabara {cadena}, es palindroma: {es_palindromo(cadena)}')