"""Función que sume o multiplique numeros complejos
"""
def sumaymultiplicacion_complejo(Real1, Imag1, Real2, Imag2, A):#validación de entradas y asignación de suma A = 1 o multiplicación A = 2
    if isinstance (Real1, int) and (Real2, int) and isinstance (Imag1,complex) and (Imag2, complex):
        return principal_complejo(Real1, Imag2, Real2, Imag2, A)
    else:
        return "Los números no son válidos"

def principal_complejo(Real1, Imag1, Real2, Imag2, A):#Función que suma o multiplica los números complejos
    if A == 1:
        Suma = Imag1 + Imag2
        return Suma
    else:
        Multiplicación = (Real1+Imag1)*(Real2+Imag2)
        return Multiplicación
    

"""Función Regla de 3 directa
"""
def regla_directa(A, B, C):
    if isinstance (A, int) and (B, int) and (C, int):
        Regladirecta = (A*C)/B
        return Regladirecta

"""Función Regla de 3 indirecta
"""
def regla_indirecta(A, B, C):
    if isinstance (A, int) and (B, int) and (C, int):
        Reglaindirecta = (B*C)/A
        return Reglaindirecta
