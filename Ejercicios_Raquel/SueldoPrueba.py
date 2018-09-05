sueldo=input("Indique su sueldo actual en dólares: ")
def obtenerSueldo(sueldo):
    if(sueldo<1000):
        nuevoSueldo=sueldo*1.25
    elif(1000<=sueldo<=1500):
         nuevoSueldo=sueldo*1.21
    else:
        nuevoSueldo=sueldo*1.18
    print("nuevoSueldo: ", nuevoSueldo)
    #sueldo=int(input("Indique su sueldo actual en dólares: "))
    """
    Funcionalidad:Definir el nuevo sueldo del los empleados
    Entradas: sueldo(int)
    Salidas:El texto de indica el nuevo sueldo
    """

    
    
