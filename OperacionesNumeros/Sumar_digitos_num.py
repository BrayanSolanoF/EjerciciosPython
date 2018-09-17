#*****************************************************************************************
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_sumar_digitos de un entero
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 12/2018
#Entradas: Numero 
#Restricciones: El numero debe ser entero
#Salida: Suma de los digitos de el numero entero


#****************************************************************************************


def suma_dig(num):
    if (num ==0):
        return 0
    else:
        return num%10  + suma_dig(num//10)





