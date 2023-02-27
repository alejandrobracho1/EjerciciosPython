# Valores para dibujar la tabla
ANCHO = 40
RELLENO1 = '-'
RELLENO2 = ' '
CADENA_VACIA = ''


#############################################################

#Mensajes a Mostrar 
MENSAJE_INICIAL = "RADAR DE VELOCIDAD"

#############################################################

#Declaracion de variables 
velocidad = 0.0
frecuencia0 = 2e-10
frecuencia1 = 2.0000004e-10

#Formato de Salida Final en Pantalla 
FORMATO_Respuesta = ">>> La Velocidad es: %0.2f millas/hora."

#############################################################

#Encabezado del programa 
#LINEA 1: Parte superior de la tabla 
print(CADENA_VACIA.center(ANCHO, RELLENO1))
#Mensaje centrado 
print(MENSAJE_INICIAL.center(ANCHO, RELLENO2))

#############################################################

#inicio del programa :
#Calculo de la VELOCIDAD del radar 
#velocidad = 6.685x10^8 x (f1 - f0) / (f1 + f0)

velocidad = 6.685e8*(frecuencia1 - frecuencia0) / (frecuencia1 + frecuencia0)

#LINEA 2: Separador de la tabla 
print(CADENA_VACIA.center(ANCHO, RELLENO1))
#Se muestra el mensaje en pantalla 
print(FORMATO_Respuesta.center(ANCHO, RELLENO2) % (velocidad))

#LINEA 3: Parte inferior de la tabla 
print(CADENA_VACIA.center(ANCHO, RELLENO1))