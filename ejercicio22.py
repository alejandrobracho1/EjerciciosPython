#ESTRUCTURAS REPETITIVAS 
#TABLA DE POTENCIAS

#Variables 
numero = 0 
potencia = 0

#lectura de datos

numero = int(input(">>> Ingrese un numero "))

i = 1
while (i < 10):
    potencia = numero ** i
    print("%d elevado al %d = %d" %(numero,i,potencia))
    i += 1



    
    # Solicitud de Datos
numero = int(input('>>> Introduce el numero a elevar: '))
 
for potencia in range(1,11):
    resultado= numero ** potencia
    print("%d elevado a %2d es %d"%(numero,potencia,resultado))