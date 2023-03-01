#NUMEROS EN FORMA CRECIENTE 
#NUMEROS PARES ENTRE 0 Y 200 

#Calculos 

i = 1
while i < 200:
    if i % 2 == 0:
        print("%d" %(i))
    i += 1


print('Imprimir los numeros pares entre 0 y 200 de forma Creciente')
 
for pares in range(0,201):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)