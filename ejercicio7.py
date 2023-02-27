#Declaracion de variables
radio = 0.0
area = 0.0
PI = 3.1416

#Solicitud de datos 
print("AREA DEL CIRCULO")
radio = float(input("Ingrese la medida del radio del circulo: "))

#Calculos
area = PI*(radio**2)

#Salida
print("El area del circulo es: %0.2f"% (area))