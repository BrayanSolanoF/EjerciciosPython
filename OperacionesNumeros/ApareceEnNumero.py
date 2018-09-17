#*****************************************************************************************
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_Suma_listas_anidadas
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 12/2018
#Entradas:Numeros en forma de lista
#Restricciones: Los numero deben ingresar en forma de lista
#Salida: resulatdo entero de la suma de los valores en la lista


#****************************************************************************************


def aparece(num, dig):
    if ((isinstance(num,int) and isinstance(dig, int)
         and dig >= 0 and dig<=9 and num>0)):
        return aparece_aux(num, dig)
    else: return "Error"
def aparece_aux(num, dig):
    if num == 0:
        return 0
    elif num % 10 == dig:
        return 1 + aparece_aux(num // 10, dig)
    else: return aparece_aux(num//10, dig)
        





