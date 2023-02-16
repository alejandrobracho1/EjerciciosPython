nombre = (input("Introduzca su nombre: "))
apellido = (input("Introduzca su apellido: "))

#print("Hola ", {nombre}, {apellido}, ", gusto en conocerte") 
print(f"Hola {nombre} {apellido}, gusto en conocerte") 

# OTRAS MANERAS

#Declaracion de variables 
nombre = ""
apellido = ""

#Solciitud de datos 
print(">>>Introduzca su nombre: ")
nombre = input("> ")
print(">>>Introduzca su apellido: ")
apellido = input("> ")

#Mostrar datos con operador de formato %
print("Hola %s %s, gusto en conocerte!" %(nombre, apellido))






# Declaracion de variables
nombre = ""
apellido = ""
 
# Solicitud de Datos
print(">>> Introduce tu nombre: ")
nombre = input("> ")
print(">>> Introduce tu apellido: ")
apellido= input("> ")
 
# Mensaje en Pantalla: Metodo .format()
print("Hola {0} {1}, gusto en conocerte!".format(nombre,apellido))




# Declaracion de variables
nombre = ""
apellido = ""
 
# Solicitud de Datos
print(">>> Introduce tu nombre: ")
nombre = input("> ")
print(">>> Introduce tu apellido: ")
apellido= input("> ")
 
# Mensaje en Pantalla: f-strings
print(f"Hola {nombre} {apellido}, gusto en conocerte!")
