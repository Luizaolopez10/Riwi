
""" 6. ADIVINA UN NUMERO """
""" Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto. """

numero = int(input("por favor ingresa un numero entero : ")); 
print(f"el numero que ingresaste fue {numero}");
intentos =0;

while intentos<3:
    
    if numero == 6:
        print ("felicidades, encontraste el numero magico");
        break;
    
    else:
        print("sigue intentando");
        numero = int(input("intenta de nuevo, Ingresa un numero entero: "));
        intentos += 1;
        
        if intentos ==3:
            print("haz alcanzado el numero maximo de intentos");
            
            break;
    
    
    

   
    



        



      
    
    
       
