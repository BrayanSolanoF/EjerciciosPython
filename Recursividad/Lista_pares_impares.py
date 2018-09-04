def pares_impares(lista):
    if not isinstance(lista,list) or lista==[]:
        return None
    return pares_impares_aux(lista,[],[])
def pares_impares_aux()



def par_aux(List):
    if List!=[]:
        if List[0]%2==0:
            return[List[0]] + par_aux(List[1:]) #La operacion en el return me garantiza la recursividad de pila
        else:
            return par_aux(List[1:])
    else:
        return []
def imp_aux(List):
    if List!=[]:
        if List[0]%2 == 1:
            return [List[0]]+ imp_aux(List[1:])
        else:
            return imp_ax(List[1:])
    else:
        return[]

