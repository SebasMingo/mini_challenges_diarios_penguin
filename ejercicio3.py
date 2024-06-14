vocales = ["a","e","i","o","u"] #Esta en una lista que tiene por nombre "vocales" que contiene vocales

palabra = input("Ingrese una palabra") #Aqui pedimos al usario que ingrese una palabra a ser evaluada

contador_vocales = 0 #declaro la variable del contador en cero 

for vocal in palabra: #Para cada vocal en la palabra ingresada 
    if vocal in vocales: #Si es que una vocal de la palabra ingresada esta en la lista vocales
        contador_vocales +=1 #El contandor aumenta en 1 


print(f"El total de vocales es de: {contador_vocales}") #Imprime El total de vocales que se han encontrado





