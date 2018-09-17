#*****************************************************************************************
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_Cantidad_de_digitos_en_lista_anterior
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 12/2018
#Entradas:Numeros en forma de lista
#Restricciones: Los numero deben ingresar en forma de lista
#Salida: Nueva lista con la cantidad de digitos en posicion de la lista anterior


#****************************************************************************************
# [0,245,5] = input
# [1,3,1] = output

def cantidad(lista):
    if isinstance(lista, list)and(lista!=[]):
        return cantidad_aux(lista)
    else:
        return "Error"

def cantidad_aux(lista):
    if lista==[]:
        return []
    else:
        return [cantidad_aux2(lista[0], False)]+cantidad_aux(lista[1:])


def cantidad_aux2(num, validador):
    if num==0 and validador:
        return 0
    else:
        return 1+cantidad_aux2(num//10, True)
