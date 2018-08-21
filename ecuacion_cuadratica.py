#Programa: fun Ecuacion cuadratica
#Entrada: valores de a,b y c
#Salida:Raices de la ecuacion x1 y x2
#Restricciones:No
#version:2.0
#Formula: ax al cuadrado + bx + c, con a diferente de cero, b y c son reales
#x=(-b(+-)Raiz(b**2-4+a*c))/2a
from math import sqrt
def ecuacion_cuadratica(a,b,c):
        Raiz = sqrt(b**2-4*a*c)
        Raiz1 = (-b+ Raiz)/(2*a)
        Raiz2 = (-b-Raiz)/(2*a)
        return Raiz1, Raiz2
    
