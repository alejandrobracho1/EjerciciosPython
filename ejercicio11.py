#Declaracion de variables 
numero = 0

#Lectura de datos 
numero = int(input("Ingrese el numero entero: "))

#Calculos 
if int(numero) == 0:
    print("El número no es Positivo ni Negativo.")
elif int(numero) < 0:
    print("El numero es negativo")
elif int(numero) > 0:
    print("El numero es positivo")
    
    
    # Declaracion de variables
numero = 0
 
# Solicitud de Datos
numero = float(input('>>> Ingrese un numero: '))
 
# Condiciones para saber si el numero es Positivo o Negativo
if numero == 0:
    print('El numero no es Positivo ni Negativo.')
elif numero < 0:
    print('El numero es Negativo.')
else:
    print('El numero es Positivo.')