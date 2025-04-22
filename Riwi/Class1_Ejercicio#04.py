

"""4.CONTRASEÑA CORRECTA"""
"""pide una contraseña al usuario, si conincide con "python123", imprime "acceso concedido, de lo contrario "contraseña incorrecta" """


print("por favor ingresa tu contraseña"); # imprime un mensaje

contraseña = input(); # se le pide al usuario que ingrese una contraseña

print ("la contraseña que ingresaste es: " + contraseña); # imprime un mensaje

if contraseña == "python123":{ # validamos si la contraseña que ingreso el usuario y que se almaceno en la variable contraseña es igual a "python123"
    
    print("Acceso Concedido") # se imprime un mensaje 
}
else:{ # si no es todo lo contrario del SI
    
    print("contraseña incorrecta") # se imprime un mensaje
} 