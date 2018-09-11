def cont_pares(lista):
    if isinstance(lista, list) or lista!=[]:
        return cont_pares_aux(lista,0)
    else:
        return"Error"
def cont_pares_aux(lista, contador):
    if lista==[]:
        return 0
    if contador > 2:
        return True
    if lista[0]%2==0:
        return cont_pares_aux(lista[1:], contador+1)
    else:
        return cont_pares_aux(lista[1:], contador)


