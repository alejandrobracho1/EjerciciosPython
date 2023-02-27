#Declaracion de variables 
celcius    = 0.0
fahrenheit = 0.0

#Solicitud de Datos 
fahrenheit = float(input("Ingrese los grados fahrenheit: "))

#Calculos de datos 
celcius = ((fahrenheit - 32.0) * 5.0) / 9.0

#Salida de datos 
print("Los grados en fahrenheit: %0.2f"% (fahrenheit) + " en celcius son: %0.2f"%(celcius))
