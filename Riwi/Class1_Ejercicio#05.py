
""" 5. CALCULADORA DE PROPINAS """

""" Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina. """

print("ingresa el valor total de la cuenta");
cuenta = str(input());
print(f"el valor ingresado fue: {cuenta}","$");

print("que porcentaje de propina deseas dejar 10%, 15%, 20% ?");
porcentaje = int(input());
print(f"el valor del porcentaje de descuento que ingreso el usuario fue: {porcentaje}"," % ");



propina = float (cuenta)*(porcentaje/100);

print("la propina fue de:"+format(propina,".3f"),"$") ;

