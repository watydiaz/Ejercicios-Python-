"""
Ejercicio 2: Calculadora de área de círculo
Escribe una función area_circulo que acepte un argumento de radio y calcule el área del círculo correspondiente. Recuerda que el área de un círculo se calcula como pi * radio**2.
"""

def saludar(nombre):
    mensaje = f"Hola, {nombre}, ¡Bienvenido!"
    return mensaje

nombre = input('Ingrese su nombre: ')
saludo = saludar(nombre)
print(saludo)

def area_circulo(radio):
    pi = 3.14159
    area = pi * (radio**2)
    return area

radio = float(input(f'{nombre} Ingrese el radio del círculo: '))
area = area_circulo(radio)
print(f' {nombre} El área del círculo con radio {radio} es: {area}')
