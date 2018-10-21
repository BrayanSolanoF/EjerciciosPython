def insert_sort(lista):
    return insert_sort_aux(lista,1,len(lista))
def insert_sort_aux(lista,i,n):
    if i==n:
        return lista
    Aux=lista[i]
    j=incluye_orden(lista,i,Aux)
    lista[j]=Aux
    return insert_sort_aux(lista,i+1,n)
def incluye_orden(lista,j,Aux):
    if j<=0 or lista[j-1]<=Aux:
        return j
    lista[j]=lista[j-1]
    return incluye_orden(lista,j-1,Aux)
