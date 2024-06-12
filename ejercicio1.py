def invertir_cadena(cadena): #  Define una función llamada `invertir_cadena` que recibe una cadena (`cadena`) como argumento
    cadena_invertida = "" # Inicializa una cadena vacía `cadena_invertida` para almacenar la cadena invertida
    for caracter in cadena: # Recorre cada caracter en la cadena original (`cadena`)
        cadena_invertida = caracter + cadena_invertida # Agrega el caracter actual al inicio de `cadena_invertida`, revirtiendo efectivamente la cadena
    return cadena_invertida # Retorna la cadena invertida
# Solicita la cadena al usuario
cadena = input("Ingrese la cadena que desea invertir: ")

# Invierte la cadena ingresada
cadena_invertida = invertir_cadena(cadena)

# Imprime la cadena invertida
print(f"Cadena invertida: {cadena_invertida}")