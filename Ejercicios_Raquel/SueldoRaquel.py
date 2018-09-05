#Elaborado por: Raquel Gutierrez Mora, versión 3.7.0
#Fecha de la creación: 1/09/2018
#Fecha de ultima modificación: 1/09/2018

#Importacion de la librería


#Definición de Funciones

def obtenerSueldo (sueldo):
    if(sueldo<1000):
        nuevoSueldo=sueldo*1.25
    elif(1000<=sueldo<=1500):
         nuevoSueldo=sueldo*1.21
    else:
        nuevoSueldo=sueldo*1.18
#sueldo=int(input("Indique su sueldo actual en dólares: "))
print("nuevoSueldo: ", nuevoSueldo)

#Programa Principal
