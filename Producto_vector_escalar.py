def producto_escalar(Escalar, Vector):
    return producto_escalar_aux(Escalar, 0, len(Vector), Vector)
def producto_escalar_aux(Escalar,i,n,Vector):
    if i == n:
        return Vector
    else:
        Vector[i]*=Escalar
        return producto_escalar_aux(Escalar, i+1, n, Vector)
