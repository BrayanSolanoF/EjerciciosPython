
#*****************************************************************************************
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_Primo
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 12/2018
#Entradas: Numero Entero
#Restricciones: Solo acepta numeros enteros
#Salida: Resultado booleano True or False


#****************************************************************************************

def primos (num):
    if isinstance(num, int):
        if num>0:
            if num!=1:
                return primos_aux(num, 2)
            else: True
        else:
            return "Debe ser mayor a cero"
    else:
        return "Debe ser un numero entero"
def primos_aux(num, divisor):
    if num == divisor:
        return True
    elif (num%divisor)==0:
        return False
    else: return primos_aux(num, divisor + 1)