def pares_list(lista):
    if not isinstance(lista,list) or lista==[]:
        return None
    else: return pares_list_aux(lista,[])
def pares_list_aux(lista, lista2):
    if lista==[]:
        return lista2
    elif lista[0]%2==0:
        return pares_list_aux(lista[1:], lista2+[lista[0]])
    else: return pares_list_aux(lista[1:], lista2)
