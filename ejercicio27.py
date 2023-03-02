#MATRICES 

# Declaracion de Variables:
Matriz = []
Fila = 3
Columna = 0
 
# Creacion de la matriz del teclado Matricial 4x4
Matriz = [['1', '2', '3', 'A'],
          ['4', '5', '6', 'B'],
          ['7', '8', '9', 'C'],
          ['*', '0', '#', 'D']]

# Se imprime la matriz en pantalla
for x in (Matriz):
    print(">>> IMPRIMIR MATRIZ  : %s" %(x))

print(">>> FILA A IMPRIMIR  : %s" %(Matriz[Fila]))
print(">>> DATO A IMPRIMIR  : %s" %(Matriz[Fila][Columna]))
