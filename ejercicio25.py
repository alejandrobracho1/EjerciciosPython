#IMPRIMIR PARES HASTA UN NUMERO DADO 
#Escribir un programa que imprima los números pares de forma creciente hasta un número introducido por el usuario.

numero = 0

#Lecutra de datos 
numero = int(input(">>> Instroduzca un numero: "))

if numero % 2 == 0:
    i = 1
    while i <= numero:
        if i % 2 == 0:
            print(i)
        i += 1
else:
    print("El numero debe ser PAR")



# Solicitud de Datos
numero = int(input('>>> Introduce un numero: '))
 
for pares in range(0,numero + 1):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)