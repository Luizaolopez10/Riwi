
""" CLASIFICACION DE IMC """
""" Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra:

"Bajo peso" si es menor a 18.5
"Normal" si está entre 18.5 y 24.9
"Sobrepeso" si está entre 25 y 29.9
"Obesidad" si es mayor o igual a 30

"""

peso = int(input(" por favor ingresa tu peso :"));
print(f" haz ingresado {peso} KG");

altura = float(input(" por favor ingresa tu altura:"));
print(f" haz ingresado {altura} CM");

calculo = peso/altura*altura;

print(f" tu IMC es de: {calculo}");

if calculo < 18.5:
    print("Tienes bajo peso")
elif calculo >= 18.5 and calculo<24.9:
    print("Tienes un peso normal");
elif calculo >25 and calculo <29.9:
    print("Tienes sobre peso");
elif calculo >=30:
    print("Tienes obesidad");
