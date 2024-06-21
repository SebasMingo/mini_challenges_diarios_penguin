#Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable (entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas, números y símbolos.

import random

# Definir las listas de caracteres
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%^&*()-_+="

# Unir todas las listas en una sola
todos_caracteres = mayusculas + minusculas + numeros + simbolos

# Pedir al usuario que ingrese la longitud de la contraseña
longitud = int(input("Ingrese la longitud de la contraseña (entre 8 y 16): "))

# Verificar que la longitud esté dentro del rango permitido
while longitud < 8 or longitud > 16:
    longitud = int(input("Longitud inválida. Ingrese un número entre 8 y 16: "))

# Inicializar la contraseña como una lista vacía
contraseña = []

# Asegurar al menos un carácter de cada tipo
contraseña.append(random.choice(mayusculas))
contraseña.append(random.choice(minusculas))
contraseña.append(random.choice(numeros))
contraseña.append(random.choice(simbolos))

# Rellenar la contraseña con caracteres aleatorios hasta alcanzar la longitud deseada
for _ in range(4, longitud):
    contraseña.append(random.choice(todos_caracteres))

# Mezclar los caracteres de la contraseña
random.shuffle(contraseña)

# Convertir la lista en una cadena de caracteres
contraseña_final = ''.join(contraseña)

# Mostrar la contraseña generada
print("Contraseña generada:", contraseña_final)
