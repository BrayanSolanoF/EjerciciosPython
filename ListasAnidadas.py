#*****************************************************************************************
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_Suma_listas_anidadas
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 12/2018
#Entradas:Numeros en forma de lista
#Restricciones: Los numero deben ingresar en forma de lista
#Salida: resulatdo entero de la suma de los valores en la lista


#****************************************************************************************
def sumar(lista):
    if isinstance(lista, list):
        return sumar_lista(lista)
    else: return "El objeto ingresado no es una lista."

def sumar_lista(lista):
    if lista ==[]:
        return 0
    elif isinstance(lista[0], list):
            return sumar_lista(lista[0])+ sumar_lista(lista[1:])
        #return sumar_lista(lista[0] + lista[1:])
    else: return lista[0] + sumar_lista(lista[1:])
