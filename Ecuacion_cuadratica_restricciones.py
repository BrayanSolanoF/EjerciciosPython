#Programa: fun Ecuacion cuadratica
#Entrada: valores de a,b y c
#Salida:Raices de la ecuacion x1 y x2
#Restricciones:No
#version:2.0
#Formula: ax al cuadrado + bx + c, con a diferente de cero, b y c son reales
#x=(-b(+-)Raiz(b**2-4+a*c))/2a
#Agregar un if para verificar si a es diferente de 0 y cumplir la condicion de cuadratica
from math import sqrt
def ecuacion_cuadratica(a,b,c):
    if a != 0:
        Discriminante = (b**2-4*a*c)
        if Discriminante > 0:
            Raiz = sqrt(b**2-4*a*c)
            Raiz1 = (-b+ Raiz)/(2*a)
            Raiz2 = (-b-Raiz)/(2*a)
            return Raiz1, Raiz2
        else:
            return "Ecuaciòn con Raices imaginarias"
    else:
        return "La ecuacion no es cuadratica"
    
