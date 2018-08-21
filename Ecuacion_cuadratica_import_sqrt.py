#Programa: fun Ecuacion cuadratica
#Entrada: valores de a,b y c
#Salida:Raices de la ecuacion x1 y x2
#Restricciones:No
#version:2.0
#Formula: ax al cuadrado + bx + c, con a diferente de cero, b y c son reales
#x=(-b(+-)Raiz(b**2-4+a*c))/2a
#Agregar un if para verificar si a es diferente de 0 y cumplir la condicion de cuadratica
from math import sqrt
def ecua_cuadratica(A,B,C):
    if A != 0: #verificar si A diferente de cero
        Discriminante = (B**2-4*A*C)
        if Discriminante > 0:
            Raiz = sqrt(Discriminante)
            Raiz1 = (-B + Raiz)/(2*A)
            Raiz2 = (-B - Raiz)/(2*A)
            return Raiz1, Raiz2
        else:
            return "El discriminantes menor a cero, Ecuaciòn con Raices imaginarias"
    else:
        return "La ecuacion no es cuadratica"
    
