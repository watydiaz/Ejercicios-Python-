'''
1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
'''
a=input('Ingrese el numero a: ')
b=input('Ingrese el numero b: ')


def mayor (a,b):
    if a>b :
        print (f'el numero mayor es {a}')
    elif b>a:
        print  (f'el numero mayor es {b}')
mayor (a,b)