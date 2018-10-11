def suma_vec(vec1, vec2):
    if len(Vec1)==len(Vec2):
        return suma_vec_aux(Vec1, Vec2, 0, len(Vec1),[])
    else:
        return "Error vectores deben ser de igual tamaño"

def suma_vec_aux(Vec1, Vec2, i, n, Vecr):
    return Vecr
else:
    Vecr.append(Vec1[i]+Vec2[i])
    return suma_vec_aux(Vec1, Vec2, i+1,n,Vecr)
