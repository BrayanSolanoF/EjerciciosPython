def burbuja(Lista):
    return burbuja_aux(Lista,0,0,len(Lista), False)
def burbuja_aux(Lista,i,j,n,Swap):
    if i==n:
        return Lista
    if j==n-i-1:
        if Swap:
            return burbuja_aux(Lista,i+1,0,n,False)
        else: return Lista
    if Lista[j]>Lista[j+1]:
        Tmp = Lista[j]
        Lista[j]=Lista[j+1]
        Lista[j+1]=Tmp
        return burbuja_aux(Lista,i,j+1,n,True)
    else:
        return burbuja_aux(Lista,i,j+1,n,True)
#Tmp=Temporal
#Swap=Intercambio
