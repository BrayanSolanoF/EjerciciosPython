def cantidad(lista):
    if isinstance(lista, list)and(lista!=[]):
        return cantidad_aux(lista)
    else:
        return "Error"

def cantidad_aux(lista):
    if lista==[]:
        return []
    else:
        return [cantidad_aux2(lista[0])]+cantidad_aux(lista[1:])


def cantidad_aux2(num):
    if num==0:
        return 0
    else:
        return 1+cantidad_aux2(num//10)
