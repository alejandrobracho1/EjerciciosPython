#MATRIZ NULA 
Matriz = []
fila = 0
columna = 0 

#Lectura de datos 
fila = int(input(">>> Ingrese el numero de filas de la matriz: "))
columna = int(input(">>> Ingrese le numero de colunas de la matriz: "))


Matriz = []
# Se agregan los elementos a la Matriz
for elemento in range(fila):
    Matriz.append ([0] * columna)

for x in (Matriz):
    print(">>> MATRIZ: (%dx%d)"%(fila, columna), Matriz)







# Declaracion de Variables:
Longitud = 0
m_filas = 0
n_columnas = 0
 
######################################################################
 
# Pedimos la dimensión de la matriz:
m_filas    = int(input(">>> Numero de filas (m): "))
n_columnas = int(input(">>> Numero de columnas (n): "))
 
# Se crea la matriz nula
M = []
 
# Se agregan los elementos a la Matriz
for elemento in range(m_filas):
    M.append ([0] * n_columnas)
 
# Longitud de la Matriz
Longitud = len(M)
 
######################################################################
 
print("\n>>> MATRIZ M(%dx%d): %s\n" %(m_filas,n_columnas,M))
 
# Se imprime cada fila de la matriz
for fila in range(Longitud):
    print(M[fila])