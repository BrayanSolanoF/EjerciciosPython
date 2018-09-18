"""
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 09/2018
#Entradas:
#Restricciones: 
#Salida: 


"""
#1
#Entradas: Numero Enteros
#Restricciones: Numeros >=3 y <=20
#Salidas: Coseno de un angulo

def facto(X):
    if isinstance(X, int):
        return facto_aux(X)
    else:
        return "Debe ser de tipo entero"
def facto_aux(X):
    if  X>=3 and X<=20:
        return (X) + facto_aux(X-1)
    else: return (X//10)

