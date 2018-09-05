#Elaborado por: Raquel Gutierrez Mora, versión 3.7.0
#Fecha de la creación: 1/09/2018
#Fecha de ultima modificación: 1/09/2018

#Importacion de la librería


#Definición de Funciones
sueldo = input("Indique su sueldo actual en dólares:-")
def obtenerSueldo(sueldo):
    """
    Funcionalidad:Definir el nuevo sueldo del los empleados
    Entradas: sueldo(int)
    Salidas:El texto de indica el nuevo sueldo
    """
    if(sueldo<1000):
        nuevoSueldo=sueldo*1.25
    elif(1000<=sueldo<=1500):
         nuevoSueldo=sueldo*1.21
    else:
        nuevoSueldo=sueldo*1.18
    return nuevoSueldo
    print(nuevoSueldo)
#sueldo = input("Indique su sueldo actual en dólares:-")
#print(nuevoSueldo)
#print("Su sueldo anterior es: " + str(sueldo))
#+ "Su nuevo sueldo es: " + str(nuevoSueldo)

#Programa Principal





