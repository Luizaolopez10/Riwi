

""" 1. MENOR DE 3 NUMEROS """
""" Pide tres números al usuario.
Usa condicionales (if) para decir cuál es el más pequeño. """

numero1 = int(input(" ingresa el primer numero: "));
print(f"el numero que ingresaste es: {numero1}");
print("---------------------------------------------");

numero2 = int(input(" ingresa el segundo numero: "));
print(f"el numero que ingresaste es: {numero2}");
print("---------------------------------------------");

numero3 = int(input(" ingresa el tercer numero: "));
print(f"el numero que ingresaste es: {numero3}");
print("---------------------------------------------");

if numero1 < numero2 and numero1 < numero3:
    print(f"{numero1} es el numero menor de los tres");
elif numero2 < numero1 and numero2 < numero3:
    print(f"{numero2} es el numero menor de los tres");
elif numero3 < numero1 and numero3 < numero2:
    print(f"{numero3} es el numero menor de los tres");
