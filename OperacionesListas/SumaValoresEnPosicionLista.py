#*****************************************************************************************
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_sumaValoresEnLista
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 12/2018
#Entradas:Numeros en forma de lista
#Restricciones: Los numero deben ingresar en forma de lista
#Salida: Lista con suma de los valores por posicion


#****************************************************************************************
def cant_digitos(lista):
    if not isinstance (lista,list) or lista==[]:
        return None
    else: return cant_digitos_aux(lista, [])
def cant_digitos_aux(lista, lista2):
    if lista == []:
        return lista2
    elif lista[0] == 0:
        return cant_digitos_aux(lista[1:], lista2 + [1] )
    elif isinstance (lista[0], int):
        return cant_digitos_aux(lista[1:], lista2+[lista[0]%10 + (lista[0]//10)])
    else: return cant_digitos_aux(lista[1:], lista2)
