#*****************************************************************************************
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_Pares_Impares
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 12/2018
#Entradas: Numero
#Restricciones: Numero entero y mauor a cero
#Salida: 


#****************************************************************************************

def pares_impares(num):
    if isinstance (num, int) and num>0:
        return pares(num), impares(num)
    else: return "Error"
def pares(num):
    if num==0:
        return 0
    elif ((num%10)%2==0):
        return 1 + pares(num//10)
    else: return pares(num//10)
def impares(num):
    if num==0:
        return 0
    elif ((num%10)%2==1):
        return 1 + impares(num//10)
    else: return impares(num//10)
    





