def Puntos_Recta(N, Tupla1, Tupla2):
    if isinstance(N, int) and N > 0 and isinstance(Tupla1, tuple) and isinstance(Tupla2, tuple):
        pendiente = (Tupla1[1] - Tupla2[1]) / (Tupla1[0] - Tupla2[0])
        interseccion = Tupla1[1] - pendiente * Tupla1[0]
        return aux_Puntos(N, pendiente,interseccion, [])
    else:
        return "Error"


def aux_Puntos(N, pendiente, interseccion, Result):
    if N == 0:
        return Result
    else:
        return aux_Puntos(N - 1, pendiente, interseccion, Result + [(N,pendiente * N + interseccion)])
                                               
