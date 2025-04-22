

"""3. PAR O IMPAR """
"""pide un numero entero, indica si es par o impar"""


print("ingresa un numero entero"); # imprime un mensaje

numero = int(input()); # le pedimos al usuario que ingrese un valor de tipo entero

print (f"haz ingresado el numero {numero} "); # se imprime un mensaje mostrando el numero ingresado 

if numero %2 ==0:{ # validamos que el numero ingresado por el usuario sea modulo de 2 o igual a cero para determinar si el numero es par o impar
    # lo que hace este signo de % es devolver lo que sobra de una division
    
    print("el numero es par") # se imprime un mensaje
}
else:{ # si no, es lo contrario de Si
    
    print("el numero es impar") # se imprime un mensaje
} 