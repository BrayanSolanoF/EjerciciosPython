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
def valida(Vec1,Vec2):
    if Vec1 == [] and Vec2 == []:
        return True
    elif Vec1[0] <= 3 and Vec2[0] <= 3:
        return valida(Vec1[1:], Vec2[1:])
    else:
        return False
def suma_vect(Vec1, Vec2):
    if valida(Vec1, Vec2) == True:
        if len(Vec1) == len(Vec2):
            return suma_vec_aux(Vec1, Vec2, 0, len(Vec1),[])
        else:
            return "Error"
    else:
        return "Error: vectores deben ser igual de tamaño"
def suma_vec_aux(Vec1,Vec2,i,n,Vecr):
    if i == n:
        return Vecr
    else:
        Vecr.append(Vec1[i]+Vec2[i])
        return suma_vec_aux(Vec1,Vec2, i+1, n, Vecr)
#print(suma_vect([1,2,3],[3,2,1]))
#print(valida([1,2,3],[3,1,2]))

def producto_escalar(Escalar,Vector):
    return producto_escalar_aux(Escalar, 0, len(Vector), Vector)


def producto_escalar_aux(Escalar, i, n, Vector):
    if i == n:
        return Vector
    else:
        Vector[i] *= Escalar
        return producto_escalar_aux(Escalar, i + 1, n, Vector)
#print(producto_escalar(0.5, [12,12,50,97])) #intentar que me de sin coma
#print(producto_escalar(10.5, [12,12,50,97]))

def producto_vec(Vec1, Vec2):
    if len(Vec1) == len(Vec2):
        return aux_producto_vec(Vec1, Vec2, 0 , len(Vec1), [])
    else:
        return "Error"

def aux_producto_vec(Vec1, Vec2, i, n, Result):
    if i == n:
        return Result
    else:
        Result += [Vec1[i] * Vec2[i]]
        return aux_producto_vec(Vec1, Vec2, i+1, n, Result)
#print(producto_vec([2,5,14],[1,2,2]))

#**********************************Matrices**********************************

#M = [[4,6,2],[7,9,3],[0,8,1]]
#print(M)
#M[0]
#len(M) cantidad de filas

#Suma de Matrices
#Deben tener misma dimension
def suma_Matriz(Matriz1, Matriz2):
    if isinstance(Matriz1, list) and isinstance(Matriz2, list):
        return suma_matriz_aux( Matriz1, Matriz2, len(Matriz1),len(Matriz1[0]), 0, 0)
    else:
        return "Error no son listas"

def suma_matriz_aux(Matriz1, Matriz2, n, m, i, j):
    if i == n:
        return Matriz1
    elif j == m:
        return suma_matriz_aux(Matriz1, Matriz2, n, n, i+1, 0)
    else:
        Matriz1[i][j] = Matriz1[i][j] + Matriz2[i][j]
        return suma_matriz_aux(Matriz1, Matriz2, n, m, i, j+1)
#Aca cambia mas rapido j
#print(suma_Matriz([[8,9,5],[4,2,1],[5,5,5]],[[1,2,4],[2,4,1],[5,4,3]]))   
        
#def suma_matriz_aux(Mat1, Mat2, n, m, i, j, Vecr):

def traspuesta(Matriz):
    return traspuesta_aux(Matriz, len(Matriz), len(Matriz[0]),0,0,[],[])
def traspuesta_aux(Matriz, n, m, i, j, Vec, Result):
    if j == m:
        return Result
    elif i == n:
        Result.append(Vec)
        return traspuesta_aux(Matriz, n, m, 0, j + 1, [], Result)
    else:
        Vec.append(Matriz[i][j])
        return traspuesta_aux(Matriz, n, m, i+1, j, Vec, Result)
    
#print(traspuesta([[8,9,4],[2,1,8],[7,5,6]]))


def mult_vec(Vec, Matriz):
    if len(Vec) == len(Matriz[0]):
        return mult_vec_mat_aux(Vec, traspuesta(Matriz), len(Matriz[0]), len(Matriz), 0, 0, 0, [])
    else:
        return "Error"

def mult_vec_mat_aux(Vec, Matriz, n, m, i, j, Suma, Result):
    if i == n:
        return Result
    elif j == m:
        Result.append(Suma)
        return mult_vec_mat_aux(Vec, Matriz, n, m, i + 1, 0, 0, Result)
    else:
        Suma += Vec[i] * Matriz[i][j]
        return mult_vec_mat_aux(Vec, Matriz, n, m, i, j+1, Suma, Result)

#print(mult_vec([2,2,2], [[3,4,2],[1,3,8],[2,4,6]]))
    """
Desafio

def mult_mat(Mat, Vec):
    if len(Mat[0]) == len(Vec):
        return aux_mult()
    """
def mult_mat_mat(Matriz1, Matriz2):
    # R: martriz nxp y pxm
    if len(Matriz1[0]) == len(Matriz2):
        return mult_mat_mat_aux(Matriz1, Matriz2, len(Matriz1), 0, [])
    else:
        return "Error"
def mult_mat_mat_aux(Matriz1, Matriz2, n, i, Result):
    if i == n:
        return Result
    else:
        Result.append(mult_vec(Matriz1[i], Matriz2))
        return mult_mat_mat_aux(Matriz1, Matriz2, n, i +1, Result)

#print(mult_mat_mat([[5,2],[2,5]],[[3,4],[5,2]]))
    



















