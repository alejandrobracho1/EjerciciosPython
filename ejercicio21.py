#ESTRUCTURAS REPETITIVAS 
#TABLA DE MULTIPLICAR 

#Variables 
numero = 0 
resultado = 0

#lectura de datos

numero = int(input(">>> Ingrese un numero "))

i = 1
while (i < 10):
    resultado = numero * i
    print("%d x %d = %d" %(numero,i,resultado))
    i += 1


# Declaracion de variables
multiplicador = 1
resultado = 0
numero = 0
 
# Solicitud de Datos
numero = int(input('>>> Introduce el numero a multiplicar: '))
 
while multiplicador > 0 and multiplicador < 11:
    resultado = numero * multiplicador
    print("%d x %2d = %d" %(numero,multiplicador,resultado))
    multiplicador = multiplicador + 1



# Solicitud de Datos
numero = int(input('>>> Introduce el numero a multiplicar: '))
 
for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print("%d x %2d = %d" % (numero,multiplicador,resultado))