"""
Ejercicio 1: Función de Saludo
Escribe una función saludo que acepte un argumento de nombre y retorne un saludo personalizado. Por ejemplo, saludo('Alice') debería retornar '¡Hola, Alice!'.
"""

def saludar(nombre):
    mensaje = f"Hola, {nombre}, ¡Bienvenido!"
    return mensaje

nombre = input('Ingrese su nombre: ')
saludo = saludar(nombre)
print (saludo)