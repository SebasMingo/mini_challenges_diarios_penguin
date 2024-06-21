import random #importamos el modulo random el cual proporciona funciones para generar números aleatorios y hacer selecciones aleatorias.

opciones = ["papel", "piedra", "tijera"] #creamos una lista con las opciones para la computadora
eleccionUsuario = input("Ingrese piedra, papel o tijera  ") #pedimos al usuario que ingrese una opcion

eleccionCompu = random.choice(opciones) #selecciona aleatoriamente un elemento de la lista opciones y almacena la eleccion en la variable eleccionCompu

if eleccionUsuario == eleccionCompu: #si eleccionUsuario es igual a eleccionCompu
    resultado = "Empate" #guarda "Empate" en la variable resultado
elif(eleccionUsuario  == "piedra" and eleccionCompu == "tijera" or eleccionUsuario == "tijera" and eleccionCompu == "papel" or eleccionUsuario == "papel" and eleccionCompu == "piedra"): #sino si(eleccionUruario es igual a piedra y eleccion computadora es igual a tijera o eleccionUruario es igual a tijera y eleccion computadora es igual a papel o eleccionUruario es igual a papel y eleccion computadora es igual a piedra)
    resultado = "Usuario gana" #imprime Usuario Gana
else: #sino
    resultado = "Computadora gana" #imprimi "Computadora gana"


print(f"La eleccion de la computadora fue *{eleccionCompu}* y la eleccion del usuario fue de *{eleccionUsuario}* por lo tanto el resultado es {resultado}.") # imprimi el resultado con las elecciones de la computadora y del usuario