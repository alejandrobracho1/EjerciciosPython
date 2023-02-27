#Declaracion de variables 
base = 0
altura = 0
area = 0.0

#Solicitud de Datos 
print("BASE DEL TRIANGUO")
base = input("Ingrese la medida de la base: ")
altura = input("Ingrese la medida de la altura")

#Calculo de area
area = (int(base) * int(altura)) / 2 

#Salida
print("La base del triangulo es: %0.2f"%(area))
#print("La base del triangulo es: " + str(area))