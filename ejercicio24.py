#IMPRIMIR NUMERO EN FORMA DECRECIENTE


i = 200
while i > 1:
    if i % 2 == 0:
        print("%d" %(i))
    i -= 1



print('Imprimir los numeros pares entre 0 y 200 de forma decreciente')
 
for pares in range(200,-1,-1):
    if pares == int(pares/2)*2 and pares > 0:
        print(pares)