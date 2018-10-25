def busca_bin(Lista, Ele):
    return busca_bin_aux(Lista, Ele, 0, len(Lista))

def busca_bin_aux(Lista, Ele, Ini, Fin):
    if Fin < Ini:
        return False
    Mitad = (Ini + Fin)//2

    if Lista[Mitad] > Ele:
        return busca_bin_aux(Lista, Ele, Ini, Mitad - 1)

    elif Lista[Mitad] < Ele:
        return busca_bin_aux(Lista, Ele, Mitad + 1, Fin)

    else:
        return Mitad

#print(busca_bin([1,2,3,4,5,78,45],78))

def burbuja(Lista):
    return burbuja_aux(Lista,0,0,len(Lista), False)
#False en caso de que haya que intercambiar

def burbuja_aux(Lista, i, j, n, Swap):
    if i == n: #Si llegue al ultimo retorne la lista
        return Lista
    if j == n - i - 1: # 
        if Swap:
            return burbuja_aux(Lista, i+1, 0,n, False)
        else:
            return Lista
    if Lista[j] > Lista[j + 1]:
        Tmp = Lista[j]
        Lista[j] = Lista[j + 1]
        Lista[j+1] = Tmp
        #print(Lista, i ,j+1, n, True)
        return burbuja_aux(Lista, i ,j+1, n, True)
    else:
        return burbuja_aux(Lista, i, j+1, n, Swap)

#print(burbuja([10,2,3,8]))
#print(burbuja([10,9,5,2,85,12,2,3,8]))
def seleccion(Lista):
    return seleccion_aux(Lista,0,len(Lista))
def seleccion_aux(Lista, i ,n):
    if i == n:
        return Lista
    Min = menor(Lista, i + 1, n, i)
    Tmp = Lista[i]
    Lista[i] = Lista[Min]
    Lista[Min] = Tmp
    return seleccion_aux(Lista, i + 1, n)

def menor(Lista, j, n, Min):
    if j == n:
        return Min
    if Lista[j] < Lista[Min]:
        Min = j
        return menor(Lista, j+1, n, Min)
    else:
        return menor(Lista, j + 1, n, Min)

#print(seleccion([10,2,3,8,19,7,12,4,9,15])) #55 llamadas recursivas
#print(seleccion([10,2,3,8,4])) #15 llamadas recursivas
def insert_sort(Lista):
    return insert_sort_aux(Lista, 1, len(Lista))
def insert_sort_aux(Lista, i, n):
    if i == n:
        return Lista
    Aux = Lista[i]
    j = incluye_orden(Lista, i, Aux)
    Lista[j] = Aux
    print(Lista, i  , n)
    return insert_sort_aux(Lista, i + 1, n)

def incluye_orden(Lista, j, Aux):
    if j <=0 or Lista[j - 1] <= Aux:
        return j
    Lista[j] = Lista[j-1]
    return incluye_orden(Lista, j-1, Aux)

#print(insert_sort([10,2,3,8,19,7,12,4,9,15]))

def quick_sort(Lista):
    Menores = []
    Iguales = []
    Mayores = []
    if len(Lista) <=1:
        return Lista
    Pivote = Lista[-1]
    partir(Lista, 0, len(Lista), Pivote, Menores, Iguales, Mayores)
    ret = quick_sort(Menores)
    ret.extend(Iguales) #Toma un elemento de la lista y lo mete en la lista, aca se extiende con el valor del parametro
    ret.extend(quick_sort(Mayores))
    return ret

def partir(Lista, i, n, Pivote, Menores, Iguales, Mayores):
    if i == n:
        return Menores, Iguales, Mayores
    if Lista[i] < Pivote:
        Menores.append(Lista[i])
    elif Lista[i] > Pivote:
        Mayores.append(Lista[i])
    elif Lista[i] == Pivote:
        Iguales.append(Lista[i])
    return partir(Lista, i + 1, n, Pivote, Menores, Iguales, Mayores)

#print(quick_sort([2,3,1,4,8,7,9,8,2,9,2,9,5,5]))

def suma_vect(Vec1, Vec2):
    if len(Vec1) == len(Vec2):
        return suma_vec_aux(Vec1, Vec2, 0, len(Vec1),[])
    else:
        return "Error: vectores deben ser igual de tamaño"
def suma_vec_aux(Vec1,Vec2,i,n,Vecr):
    if i == n:
        return Vecr
    else:
        Vecr.append(Vec1[i]+Vec2[i])
        return suma_vec_aux(Vec1,Vec2, i+1, n, Vecr)
#print(suma_vect([1,2,3],[3,2,1]))

        


