#*****************************************************************************************
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_SumaDigitosEnteroConValidacion
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 12/2018
#Entradas:Numero
#Restricciones:NumeroEntero
#Salida: SumaDigitosDeUnNumeroEntero


#****************************************************************************************

def suma_dig(num):
    if isinstance(num, int) and (num>0):
        return suma_dig_aux(abs(num))
    else: return "Debe ingresar un numero entero"
def suma_dig_aux(num):
    if (num ==0):
        return 0
    else:
        return num%10  + suma_dig_aux(num//10)

