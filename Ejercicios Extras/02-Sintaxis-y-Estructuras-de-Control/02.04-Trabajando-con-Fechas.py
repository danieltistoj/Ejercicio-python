#####################################################################
# Trabajando con fechas                                             #
#####################################################################
#                                                                   #
#   Sintaxis: datetime.now()                                        #
#             datetime.now().date()                                 #
#             datetime.now().today()                                #
#                                                                   #
#             datetime.strptime("11-03-1998", "%d-%m-%Y").date()    #
#             print(datetime.now().strftime("%A, %d %m, %Y")        #
#                                                                   #
#####################################################################

from datetime import datetime

#Almacenamos en la variable dt1 la fecha actual del sistema
dt1 = datetime.now().date()
print("Fecha1: ", dt1)

#Almacenamos en la variable dt2 la fecha y hora actual del sistema
dt2 = datetime.now()
print("Fecha2: ", dt2)

#Convertimos un valor alfanúmerico en fecha utilizando STRPTIME
fecha = input("Escribe tu fecha de nacimiento: ")
dt3 = datetime.strptime(fecha, "%d-%m-%Y").date()

#Mostramos por pantalla una fecha formateada
print("Fecha3: ", dt3.strftime("%A, %d %B, %Y"))

#Calculos entre fechas
años = dt1.year - dt3.year 
print(f"Tienes {años} años.")
