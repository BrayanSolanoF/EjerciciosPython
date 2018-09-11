def elim_lista(lista, num):
    if isinstance(lista, list):
        return elim_lista_aux(lista, num)
    else: "Error"
def elim_lista_aux(lista, num):
    if lista==[]:
        return []
    else:
        if lista[0]==num:
            return elim_lista_aux(lista[1:], num)
        else:
            return [lista[0]] + elim_lista_aux(lista[1:], num)