######################################
"""
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_Puntos_Recta
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 26/2018
#Entradas: Un numero, dos tuplas.
#Restricciones: Numero entero y mayor que cero, dos tuplas
#Salida: Puntos de la recta segun el numero ingresado y la pendiente obtenida
"""

#Hallar los N puntos de una linea recta

def Puntos_Recta(N, Tupla1, Tupla2):
    if isinstance(N, int) and N > 0 and isinstance(Tupla1, tuple) and isinstance(Tupla2, tuple):
        pendiente = (Tupla1[1] - Tupla2[1]) / (Tupla1[0] - Tupla2[0])
        interseccion = Tupla1[1] - pendiente * Tupla1[0]
        return aux_Puntos(N, pendiente,interseccion, [], 0)
    else:
        return "Error"


def aux_Puntos(N, pendiente, interseccion, Result, x):
    if N == x:
        return Result
    else:
        return aux_Puntos(N , pendiente, interseccion, Result + [(N,pendiente * N + interseccion)], x+1)
                                               
