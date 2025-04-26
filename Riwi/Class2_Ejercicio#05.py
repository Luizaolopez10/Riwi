

""" 5. ¿ESTA EN LA LISTA DE INVITADOS? """
""" Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
Pide al usuario su nombre.
Usa if para decir si está en la lista de invitados o no. """

list = ["LUIS", "ANA", "ALEJANDRO", "LUCAS"]

nombre = str(input(" Ingresa un nombre: "));
print(f" el nombre ingresado es: {nombre}");


if nombre in list:
    print("el nombre ingresado esta en la lista");
else: print ("el nombre que ingresaste no esta en la lista de invitados");


