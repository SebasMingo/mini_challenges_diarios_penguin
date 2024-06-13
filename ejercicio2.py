numero_ingresado = int(input("Ingrese un numero a ser multiplicado")) #Se pide al usuario que ingrese un numero para que sea multiplicado

for numero in range(0,11): #Bucle for en un rango de 0 a 11(incluye el 0, pero excluye el 11, por lo que va de 0 a 10) y la variable numero almacena el valor actual de cada iteración en el rango especificado.
    total = numero_ingresado * numero #variable total es igual a la variable numero_ingresado(que almacena el numero ingresado) * numero
    print(f"{numero} * {numero_ingresado} = {total}") #imprimimos el numero
