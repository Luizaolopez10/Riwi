
""" 2.VERIFICAR SI UN NUMERO ESTA EN LA LISTA """
""" Crea una lista con 5 números.
Pide un número al usuario y verifica si está en la lista usando in. """


list = [23,14,5,3,8]

numero = int(input(" Ingresa un numero: "));
print(f" el numero ingresado es: {numero}");


if numero in list:
    print("el numero ingresado esta en la lista");
else: print ("el numero que ingresaste no esta en la lista");


