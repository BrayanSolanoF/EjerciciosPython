#*****************************************************************************************
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_fibonacci
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 12/2018
#Entradas:Numero
#Restricciones: Numero de tipo entero
#Salida: Resultado segun fibonacci


#****************************************************************************************

def fib(num):
    if isinstance(num, int):
        if num >=0:
            return fib_aux(num)
        else: return "Debe ser mayor o igual a cero"
    else: return "Debe ser un numero entero"
        
def fib_aux(num):
    if num<2:
        return num
    else:
        return fib_aux(num-1)+ fib_aux(num-2)
