'''
5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
'''

nombre = input ('Ingrese su nombre: ')
a = int(input(f'Hola, {nombre}, por favor ingrese el primer numero: '))
b = int(input(f'{nombre}, por favor ingrese el segundo numero: '))
c = int(input(f'de nuevo ingrese el tercer numero: '))
d = int(input(f'{nombre}, ingrese el ultimo numero: '))
def sum (a,b,c,d):
    suma = a + b + c + d
    return suma

def multip (a,b,c,d):
    multiplicacion = a * b * c * d
    return multiplicacion

resultado = sum(a,b,c,d)
print(f'El resultado de la suma es: {resultado}')
resultado2 = multip(a,b,c,d)
print(f'El resultado de la multiplicacion es: {resultado2}')