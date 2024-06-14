# Solicita al usuario que ingrese una serie de números separados por espacios
numeros_ingresados = input("Ingrese una serie de números separados por espacios: ")

# Divide la cadena en una lista de strings usando el método split()
numeros_str = numeros_ingresados.split()

# Verifica si todos los elementos pueden convertirse en enteros
if all(numero_str.isdigit() for numero_str in numeros_str):
    # Convierte cada elemento de la lista en un entero
    numeros = [int(num) for num in numeros_str]

    # Ordena la lista de números en orden ascendente
    numeros.sort()

    # Muestra la lista ordenada
    print("La lista ordenada es:", numeros)
else:
    print("Por favor, ingrese solo números enteros separados por espacios.")