

""" LISTA VACIA Y APPEND() """

""" Crea una lista vacía llamada nombres.
Pide al usuario su nombre y agrégalo a la lista usando append().
Muestra la lista final. """


nombres = []

nombre_nuevo = str(input("ingresa un nombre: "));
nombres.append(nombre_nuevo);

nombre_nuevo = str(input("ingresa un nombre: "));
nombres.append(nombre_nuevo);

nombre_nuevo = str(input("ingresa un nombre: "));
nombres.append(nombre_nuevo);

for nombre in nombres:
    print(f"los nombres agregados a la lista vacia son : {nombres}");
    break;





