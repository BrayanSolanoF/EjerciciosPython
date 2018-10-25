def cont_impares(lista):
    if isinstance(lista, list) or lista==[]:
        return cont_impares_aux(lista)
    else:
        return "Error"
def cont_impares_aux(lista):
    if lista ==[]:
        return 0
    elif lista[0]%2==1:
        return 1+ cont_impares_aux(lista[1:])
    else:
        return 0+ cont_impares_aux(lista[1:])
