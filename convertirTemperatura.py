"""
Ejercicio 3: Conversor de temperatura
Escribe dos funciones, celsius_a_fahrenheit y fahrenheit_a_celsius, que conviertan temperaturas de una escala a otra.
C = (5/9)*(f-32)
F = (9/5) * (C + 32)
"""
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_a_farenheit(celsius):
    far = (9/5) * celsius + 32
    return far

# Ejemplo de uso
grados_fahrenheit = float(input('Ingrese los grados Fahrenheit: '))
grados_celsius = fahrenheit_a_celsius(grados_fahrenheit)
print(f"{grados_fahrenheit} grados Fahrenheit equivalen a {grados_celsius} grados Celsius.")

grados_cel = float(input('Ingrese los grados Celsius: '))
grados_far = celsius_a_farenheit(grados_cel)
print(f"{grados_cel} grados Celsius equivalen a {grados_far} grados fahrenheit.")
