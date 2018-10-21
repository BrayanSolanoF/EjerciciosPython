######################################
"""
# Instituto Tecnologico de Costa Rica


# Ingenieria en Computadores


#Programa: fun_Puntos_Recta
#Lenguaje: Python 3.6.4
#Autor: Brayan Solano Fonseca
#Version: 1.0
#Fecha Ultima Modificacion: Septiembre 26/2018
#Entradas: Un numero entero
#Restricciones: Tipo entero ya sea positivo o negativo
#Salida: N punto de la circunferencia de un circulo
"""
###########################################
"""
Para un circulo de radio 1 hallar los N puntos de la circunferencia en el
plano cartesiano
"""

def Circulo_rad1 (Num):
    if isinstance(Num,int):
        if Num==0:
            return [(1,0)]
        elif Num<0:
            return Circulo_rad1_aux(abs(Num)/360,[])
        else:
            return Circulo_rad1_aux(Num/360,[])
    else:
        return "Debe ser un numero entero"

def Circulo_rad1_aux(Num,res):
