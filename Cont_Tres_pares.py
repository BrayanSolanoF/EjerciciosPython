"""
Determinar si una lista contiene al menos tres numeros pares
E:Una lista con elementos numericos
S:un booleano determinando si es False o True
R:Que sea una lista no vacia y elementos enteros
"""

def paresTres(lista):
    if not isinstance(lista,list) or lista==[]:
        return None
    return paresTres_aux(lista,0)

def paresTres_aux(lista,cont):
    if lista==[]:
        return 0
    if cont>2:
        return True
    if lista[0]%2==0:
        return paresTres_aux(lista[1:],cont+1)
    else:
        return  paresTres_aux(lista[1:],cont)
