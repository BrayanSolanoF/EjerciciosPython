def elim_num(Lista,num,ListaAux):
    if not isinstance(Lista,list) or Lista==[]:
        return None
    return elim_num_aux(Lista,num,ListaAux)
'''def elim_num_aux(lista,num,lista2):
    if lista==[]:
        return lista2
    elif lista[2]:'''
def elim_num_aux(Lista,Num,ListaAux):
    if Lista[0]==Num:
        ListaAux = (ListaAux+ Lista[1:])
        return ListaAux
    else:
        if Lista[1:]==[]:
            return "El numero no esta en la lista"
        else:
            ListaAux = ([Lista[0]]+ ListaAux)
            return elim_num_aux(Lista[1:],Num,ListaAux)
