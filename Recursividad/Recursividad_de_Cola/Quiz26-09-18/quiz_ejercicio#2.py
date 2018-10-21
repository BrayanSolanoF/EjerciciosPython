###################################################
"""
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_Puntos_Recta
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 26/2018
#Entradas: Numero
#Restricciones: Numero entero y mayor que 8
#Salida: Numero expresado en valores de 3 y 5
"""
####################################################
"""
Todo numero n mayor o igual que 8 se puede expresar
como una suma de treses y cincos. Es decir existen dos numeros a y b tal que :
N = 3*a + 5*b
Construya una funcion que dado un numero mayor que 8 los exprese en terminos
de treses y cincos.
"""

def Expresar_Num(Num):
    if isinstance(Num,int) and Num>=8:
        return Expresar_Num_aux(Num,0,[])
    else:
        return "Ingresar un numero mayor o igual que 8"

def Expresar_Num_aux(Num,contador,resultado):
    if Num==0:
        return resultado
    elif Num%5==0 and Num!=0:
        Num-=5
        resultado+=[5]
        return Expresar_Num_aux(Num,contador,resultado)
    else:
        Num-=3
        resultado+=[3]
        return Expresar_Num_aux(Num,contador,resultado)

