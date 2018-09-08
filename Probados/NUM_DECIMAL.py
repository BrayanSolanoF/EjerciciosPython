#Programa: fun componer un numero decimal a partir de tres digitos
#Entrada: valores de a,b y c
#Salida: Numeros como maximo de tres digitos
#Restricciones:Las entradas deben ser digitos
#version:2.0
#Formula:
def num_decimal(a,b,c):
    N1 =(a*10**2+ b*10**1+c*10**0)
    N2 =(c*10**2+b*10**1+a*10**0)
    return N1,N2
