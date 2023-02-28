#MAYUSCULA O MINUSCULAS 
#Declaracion de variables 

letra = ''

#Calculos 

letra = input(">>> Ingrese una letra: ")

if letra < 'z' and letra > 'a': #a-z (97-122)
    print('La letra es Minuscula. ')
elif letra <= 'Z' and letra >= 'A': #A_Z (65-90)
    print("La letra es Mayuscula. ")
else:
    print("El valor introducido no es una letra!")



letra2 = input("Introduzca una letra: ")

if letra2.isupper():
    print("La letra ingresada es MAYÚSCULA.")
elif letra2.islower():
    print("La letra ingresada es minúscula.")
else:
    print("No ingresó una letra.")