#EDAD DE DOS PERSONAS 
#Declaracion de variables 
edad1 = 0
edad2 = 0

#Solciitud de datos
edad1 = int(input(">>> Ingrese la edad de la primera persona: "))
edad2 = int(input(">>> Ingrese la edad de la segunda persona: "))

#Calculos 

if int(edad1) < int(edad2):
    print("la segunda persona es mayor que la primera")
elif int(edad1) > int(edad2):
    print("la primera persona es mayor que la segunda")
elif int(edad1) == int(edad2):
    print("Ambas personas tienen la misma edad")