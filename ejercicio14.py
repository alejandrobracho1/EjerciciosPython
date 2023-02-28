#MULTIPLO DE 3 
#Declaracion de variables 
numero = 0

#lectura de datos 
numero = int(input(">>> Ingrese un numero: "))

#Caculos 
if int(numero) % 3 == 0:
    print(f"El numero {numero} es divisible entre 3")
else:
    print("El numero %d no es divisible entre 3" %(numero))





# Declaracion de variables:
int_Numero = 0
 
# Solicitud de Datos 
int_Numero = int(input('>>> Introduce un numero: '))
 
if int_Numero == (int_Numero // 3) * 3:
    print("El numero %d es multiplo de 3." %(int_Numero))
else:
    print("El numero %d no es multiplo de 3." %(int_Numero))