#*****************************************************************************************
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_Cantidad_de_digitos_en_lista_anterior
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 12/2018
#Entradas:NumeroEntero
#Restricciones: Numero entero positivo
#Salida: Longitud del numero


#****************************************************************************************

def largo(num):
    if isinstance(num, int) and (num>0):
        return largo_aux(abs(num))
    else: return "Debe ser un numero entero"
def largo_aux(num):
    if (num==0):
        return 0
    else: return 1 + largo_aux(num // 10)
            







