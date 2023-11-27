'''
2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
'''

a=input('Ingrese el numero a: ')
b=input('Ingrese el numero b: ')
c=input('Ingrese el numero c: ')


def mayor (a,b,c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor

resultado = mayor(a,b,c)
print (f'el numero mayor entre {a,b,c}, es {resultado}.')