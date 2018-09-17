#*****************************************************************************************
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_Sumatoria
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 12/2018
#Entradas:Numero entero
#Restricciones: Numero de tipo entero y mayor o igual a uno
#Salida: 


#****************************************************************************************

def sumatoria(N):
    if isinstance(N,int):
        if N>=1:
            return  sumatoria_aux(N)
        else: return "Debe ser mayor que 1"
    else: return "Debe ser entero "
def sumatoria_aux(N):
    if N == 0:
        return 0
    else: return N + sumatoria_aux(N-1)







