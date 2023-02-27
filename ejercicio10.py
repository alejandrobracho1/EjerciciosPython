#Valores para dibujar en la tabla 
ANCHO = 40
RELLENO1 = '-'
RELLENO2 = ' '
CADENA_VACIA = ''

#############################################################

#Mensaje a mostrar 
MENSAJE_INICIAL = "CALCULADORA FREELANCER (USD)"

#############################################################

#Declaracion de variables 
dolar_hora = 20
hora_semanal = 40
pago_semanal = 0.0
pago_mensual = 0.0

#Formato de Salida Final en la pantalla
formato_respuesta1 = ">>> Precio en Dolares por Hora: %d"
formato_respuesta2 = ">>> PAGO SEMANAL: %0.2f"
formato_respuesta3 = ">>> PAGO MENSUAL: %0.2f"

############################################################

#Encabezado del programa
# LINEA 1: Parte Superior de la tabla 
print(CADENA_VACIA.center(ANCHO, RELLENO1))
#Mensaje centrado 
print(MENSAJE_INICIAL.center(ANCHO, RELLENO2))


############################################################

#Inicio del programa
#Calculo de pago semanal 
pago_semanal = dolar_hora * hora_semanal
pago_mensual = dolar_hora * hora_semanal * 4

#IMPRESIONES 

#Mensjes de pagos
print(CADENA_VACIA.center(ANCHO, RELLENO1))
print(formato_respuesta1 % (dolar_hora))
print(CADENA_VACIA.center(ANCHO, RELLENO1))
print(formato_respuesta2 % (pago_semanal))
print(formato_respuesta3 % (pago_mensual))
print(CADENA_VACIA.center(ANCHO, RELLENO1))