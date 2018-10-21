def seleccion(lista):
    return seleccion_aux(lista,0,len(lista))
def seleccion_aux(lista,i,n):
    if i==n:
        return lista
    Min=menor(lista,i+1,n,i)
    Tmp=lista[i]
    lista[i]=lista[Min]
    lista[Min]=Tmp
    return seleccion_aux(lista,i+1,n)
def menor(lista,j,n,Min):
    if j==n:
        return Min
    if lista[j]<lista[Min]:
        Min=j
        return menor(lista,j+1,n,Min)
