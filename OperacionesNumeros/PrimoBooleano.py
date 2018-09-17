#*****************************************************************************************
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_PrimoBooleano
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 12/2018
#Entradas:NumeroEntero
#Restricciones:  Numero de tipo entero y mayor a uno
#Salida: Resultado booleano "True" or "False"


#****************************************************************************************

def primo(N):
    if isinstance(N, int):
        if N >1:
            return primo_aux(N, N-1)
        else: return "Debe ser mayor a uno"
    else: return "Debe ser un numero entero"
def primo_aux(N, divisor):
    if divisor==1:
        return True
    elif ((N%divisor)==0):
        return False
    else:
        return primo_aux(N, divisor-1)







