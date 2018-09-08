#Programa: fun Ecuacion cuadratica
#Entrada: valores de a,b y c
#Salida:Valor de grados en fahrenheit
#version:2.0
#Formula: ax al cuadrado + bx + c, con a diferente de cero, b y c son reales
#x=(-b(+-)Raiz(b**2-4+a*c))/2a
#from  math import sqrt as raiz
#sin importar sqrt usamos elevado a la 0.5
def ecuacion_cuadratica(a,b,c):
        Raiz=((b**2-4*a*c)**0.5)
        Raiz1 = (-b+ Raiz)/(2*a)
        Raiz2 = (-b-Raiz)/(2*a)
        return Raiz1, Raiz2
    
    
