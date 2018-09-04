def mayor_aux(Lista):
    if Lista[1:]==[]:
        return Lista[0]
    else:
        return ret_mayor(Lista[0],mayor_aux(Lista[1:]))
def ret_mayor(X,Y):
    if X>Y:
        return X
    else:
        return Y
