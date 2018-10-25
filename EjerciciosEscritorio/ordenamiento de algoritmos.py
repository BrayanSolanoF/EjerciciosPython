####busqueda binaria


def busca_bin(lista,ele):
    return busca_bin_aux(lista,ele,0,len(lista)):


def busca_bin_aux(lista,ele,ini,fin):
    if fin < ini:
        return False
    mitad = (ini+fin)//2
    if lista[mitad]>ele:
        return busca_bin_aux(lista,ele,ini,mitad-1)
    elif lista[mitad]<ele:
        return busca_bin_aux(lista,ele,mitad+1,fin)
    else:
        return mitad



###ordenamiento de burbuja

def burbuja(lista):
    return burbuja_aux(lista,0,0,len(lista),False)

def burbuja_aux(lista,i,j,n,Swap):
    if i==n:
        return lista
    if j==n-i-1:
        if swap:
            return burbuja_aux(lista,i+1,0,n,False)
        else:
            return False
    if lista[i] > lista[i+j]:
        Tmp = lista[j]
        lista[j] = lista[j+1]
        lista [j+1] = Tmp
        return burbuja_aux(lista,i,j+1,n,True)
    else:
        return burbuja_aux(lista,i,j+1,n,swap)




#ordenacion por seleccion

def seleccion(lista):
    return seleccion_aux(lista,0,len(lista))

def seleccion_aux(lista,i,n):
    if i==n:
        return lista
    Min=menor(lista,i+1,n,i)
    Tmp = lista[i]
    lista[i] = lista[Min]
    lista[Min] = Tmp
    return seleccion_aux(lista,i+1,n)
def menor(lista,j,n,Min):
    if j==n:
        return Min
    if lista[j]<lista[Min]:
        Min = j
    return menor(lista,j+1,n,Min)

#ordenacion por insercion

def insert_sort(lista):
    return insert_sort_aux(lista,i,n):
        if i==n:
            return lista
    Aux = lista[i]
    j = incluye_orden(lista,i,Aux)
    lista[j] = Aux
    return insert_sort_aux(lista,i+1,n)
def incluye_orden(lista,j,Aux):
    if j <= 0 or lista[j-1] <= Aux:
        return j
    lista[j] = lista[j-1]
    return incluye_orden(lista,j-1,Aux)



#ordenacion por quicksort

