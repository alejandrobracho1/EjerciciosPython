#Longitud de matrices 

#Numero de filas 
matriz = [[1,0],[0,1],[0,0]]
print(len(matriz))

#Numero de columnas 
print(len(matriz[0]))

#Matriz 3 x 3 
M = [[1,2,3],[4,5,6],[7,8,9]]

print(">>> MATRIZ: ",M)

print(">>> FILA 1: ",M[0])
print(">>> FILA 2: ",M[1])
print(">>> FILA 3: ",M[2])


# Declaracion de Variables:
Matriz = []
Longitud = 0
 
# Creacion de la matriz 
Matriz = [[7, 8, 9], [4, 5, 6,], [7, 8, 9]]
 
# Longitud de la Matriz
Longitud = len(Matriz)
 
print(">>> MATRIZ: %s" %(Matriz))
 
# Se imprime cada fila de la matriz
for fila in range(Longitud):
    print(">>> FILA %d: %s" %(fila+1, Matriz[fila]))