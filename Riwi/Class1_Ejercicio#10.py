
""" 10. NUMERO DENTRO DE UN RANGO """

""" Pide un número al usuario. Di si está dentro del rango de 1 a 10 (inclusive). """

numero = int(input("por favor ingresa un numero : "));
print(f"el numero ingresado es: {numero}");


if 1 <= numero <=10:
    print("el numero esta dentro del rango");
else:
    print("el numero esta fuera del rango");