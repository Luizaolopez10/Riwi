

""" 4. EDAD VALIDA """

""" Pide al usuario su edad.
Si la edad es menor que 0 o mayor que 120, imprime "Edad no válida".
Si está en el rango correcto, imprime "Edad válida". """

edad = int(input(" Por favor ingresa tu edad :"));
print(f" la edad ingresada fue: {edad}");

if edad <0 or edad > 120:
    print("edad no valida");
else: print("la edad esta dentro del rango");