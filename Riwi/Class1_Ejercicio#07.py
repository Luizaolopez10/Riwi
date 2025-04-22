
""" 7. MAYOR DE DOS NUMEROS """
""" Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo. """

numero1 = int(input("por favor ingresa el primer numero: "));
numero2 = int(input("por favor ingresa el segundo numero: "));

print(f"los numeros que ingresaste fueron el numero {numero1} y el numero {numero2}");

if numero1 > numero2:
    print (f"este es el numero mayor: {numero1}");
elif numero2>numero1:
    print(f"este es el numero mayor: {numero2}");
elif numero1 == numero2:
    print("los numeros son iguales");