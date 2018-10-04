def busca_bin(lista,Ele):
    return busca_bin_aux(Lista,Ele,0,len(Lista))
def busca_bin_aux(Lista,Ele,Ini,Fin):
    if Fin < Ini:
        return False
    Mitad = (Ini+Fin)//2
    if Lista[Mitad]> Ele:
        return busca_bin_aux(Lista,Ele,Ini,Mitad-1)
    elif Lista[Mitad]<Ele:
        return busca_bin_aux(Lista,Ele,Mitad+1,Fin)
    else:
        return Mitad
    
