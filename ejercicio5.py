#Crear un Diccionario: Escribe un programa que cree un diccionario a partir de dos listas dadas: una de claves y otra de valores.

dorsal = [5, 12 , 7] #creo una lista con los dorsales de los jugadores del real madrid

jugador = ["Jude Bellingham","Eduardo Camavinga","Vinicius Junior"] #creo una lista con los jugadores del real madrid

real_madrid = {} #inicio un diccionario vacio

for i in range(len(dorsal)): #el bucle itera sobre los indices de la lista dorsales
    real_madrid[dorsal[i]] = jugador[i] #en cada iteracion, se asgina la clave y el valor correspondiente al diccionario 

print(real_madrid) #imprimimos el diccionario

