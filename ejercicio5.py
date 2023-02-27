#Declaracion de variables 
area = 0.0
lado = 0

#Solicitud de datos
print("Introduzca la medida del lado del cuadrado: ")
lado = int(input(">"))

#Calcular el area
area = lado ** 2

#Salida 
print("El area del cuadrado es: " + str(area))

# Declaracion de Variables
int_Lado = 0
int_Area = 0
 
# Inicio del Programa
print("CALCULAR EL AREA DEL CUADRADO")
 
# SOLICITUD de Datos 
int_Lado = int(input('Introduzca el valor del lado del cuadrado: '))
 
# AREA DEL CUADRADO
int_Area = int_Lado**2
 
print("El area del cuadrado es:  %d"%(int_Area))


#%s : Para hacer referencia a un string o conservar el mismo formato.
#%d : Para truncar a entero.
#%i : Para hacer referencia a un entero.
#%f : Para hacer referencia a flotante.
#%g : Para hacer referencia a genérico.

#decimal = 42.7 
#entero = 42 
#print ('%d %f %g %i' % (decimal, decimal, decimal, entero))