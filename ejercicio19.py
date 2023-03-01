#RESOLUCION DE ECUACIONES 
#Declaracion de variables 

a = 0.0     #Coeficiente principal
b = 0.0     #Termino independiente 
x = 0.0     #Incognita
resultado = ""

ANCHO = 40
MENSAJE_INICIAL = "ECUACION DE PRIMER GRADO: ax + b = 0"
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""



#Lectura de datos 

a = float(input(">>> Ingrese el valor de a: "))
b = float(input(">>> Ingrese el valor de b: "))


#Calculos 

if (a != 0): 
    x = -b/a

if (a == 0):
    if (b != 0):
        resultado = "La ecuación no tiene solución!"
    else:
        resultado = "La ecuación tiene infinita soluciones!"

#SALIDA
#Linea 1: Parte superior de la salida 
print(CADENA_VACIA.center(ANCHO, RELLENO1))
#Linea 2: Mensaje centrado 
print(MENSAJE_INICIAL.center(ANCHO, RELLENO2))
#Linea 3
print(CADENA_VACIA.center(ANCHO, RELLENO1))
#Linea 4: valor de a 
print(">>> El valor de a: %0.1f" %a)
#Liena 5: valro de b 
print(">>> El valor de b: %0.1f" %b)
#Liena 6: relleno 
print(CADENA_VACIA.center(ANCHO, RELLENO1))
#Linea 7: ecuacion 
print("ECUACION: %0.1f x + %0.1f = 0"%(a,b))
#Liena 7: relleno 
print(CADENA_VACIA.center(ANCHO, RELLENO1))
#Liena 8: solucion 
print(">>> SOLUCION: x = %0.1f"%(x))