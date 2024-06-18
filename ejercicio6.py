#Conversión de Temperatura: Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

def conversor_de_Celsius_a_Fahrenheit(): #creo una funcion para convertir de grados Celsius a Fahrenheit
    grado_celsius = float(input("Ingrese una temperatura en grado Celsius ")) #Pido al usuario que ingrese una temperatura con un numero flotante(con decimales)

    grado_Fahrenheit = 32 #guardo el numero 32 en una variable que llamo grado_Fahrenheit

    nuevo_grado = (grado_celsius * 9/5) + grado_Fahrenheit #Agrego una nueva variable a la cual la llamo nuevo_grado en la cual voy a a hacer el calculo para pasar de grados Celsius a grados Fahrenheit
    print(f"La temperatura actual en grados Fahrenheit es de: {nuevo_grado} grados Fahrenheit") # imprimo la conversion de grados

conversor_de_Celsius_a_Fahrenheit() #llamo a la funcion para hacer la conversion