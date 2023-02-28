#MAYOR DE 3 NUMEROS
#Declaracion de variables 
numero1 = 0
numero2 = 0
numero3 = 0


#lectura de datos 
numero1 = int(input(">>> Introduzca el numero 1: "))
numero2 = int(input(">>> Introduzca el numero 2: "))
numero3 = int(input(">>> Introduzca el numero 3: "))

#Calculos
if int(numero1) > int(numero2):
    if int(numero1) > int(numero3):
        print("El numero %d es mayor que el numero %d y el %d" %(numero1, numero2, numero3))
elif int(numero2) > int(numero3):
    print("El numero %d es mayor que el numero %d y el %d" %(numero2, numero1, numero3))
else:
    print("El numero %d es mayor que el numero %d y el %d" %(numero3, numero1, numero2))








# Declaracion de variables
primer_numero  = 0.0
segundo_numero = 0.0
tercer_numero  = 0.0
 
# Solicitud de datos
primer_numero  = float(input('Introduce el primer  numero: '))
segundo_numero = float(input('Introduce el segundo numero: '))
tercer_numero  = float(input('Introduce el tercer  numero: '))
 
if primer_numero > segundo_numero:
    if primer_numero > tercer_numero:
        maximo = primer_numero
    else:
        maximo = tercer_numero
else:
    if segundo_numero > tercer_numero:
        maximo = segundo_numero
    else:
        maximo = tercer_numero
 
print('>>> El numero maximo es: %5.2f' %(maximo))