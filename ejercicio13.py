#NUMERO PAR O IMPAR 
#Declaracion de variables 
numero = 0

#lectura de datos 
numero = int(input(">>> Ingrese un numero entero: "))

#Calculos 
if int(numero) % 2 == 0:
    print("El numero " + str(numero) + " es Par")
else:
    print("El numero " + str(numero) + " es Impar")
    



#Solucion 1: Operador de Formato %

# Declaracion de variables:
int_Numero = 0
 
# Solicitud de Datos
int_Numero = int(input('>>> Introduce un numero: '))
 
if int_Numero == (int_Numero // 2) * 2:
    print("El numero %d es par." %(int_Numero))
else:
    print("El numero %d es impar." %(int_Numero))



 # Solucion 2: f-strings

# Declaracion de variables:
int_Numero = 0
 
# Solicitud de Datos
int_Numero = int(input('>>> Introduce un numero: '))
 
if int_Numero == (int_Numero // 2) * 2:
    print(f"El numero {int_Numero} es par.")
else:
    print(f"El numero {int_Numero} es impar.")