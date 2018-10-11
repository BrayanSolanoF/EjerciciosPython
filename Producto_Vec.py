def producto_vec(Vec1, Vec2):
    if len(Vec1)==len(Vec2):
        return producto_vec_aux(Vec1, Vec2, 0, len(Vec1), 0)
    else:
        return "Error"
def producto_vec_aux(Vec1,Vec2,i,n,Result):
    if i == n:
        return Result
    else:
        return producto_vec_aux(Vec1, Vec2, i+1, n, Result+Vec1[i]+Vec2[i])
    
