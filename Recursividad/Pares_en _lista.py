def pares_list(lista):
    if isinstance(lista,list) or lista==[]:
        return pares_list_aux(lista,[])
    else: return "Error"
def pares_list_aux(lista, lista2):
    if lista==[]:
        return []
    elif lista[0]%2==0:
        return pares_list_aux(lista[1:], lista2+[lista[0]])
    else: return pares_list_aux(lista[1:], lista2)
