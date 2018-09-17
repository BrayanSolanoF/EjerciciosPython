def pares_impares(lista):
    if isinstance (lista, list):
        return pares_aux(lista, []), impares_aux(lista, [])
    else: return "Debe ingresar los valores en forma de lista"
def pares_aux(lista, lista2):
    if lista==[]:
        return lista2
    elif lista[0]%2==0:
        return pares_aux(lista[1:], lista2 + [lista[0]])
    else: return pares_aux(lista[1:], lista2)
def impares_aux(lista, lista2):
    if lista==[]:
        return lista2
    elif lista[0]%2 !=0:
        return impares_aux(lista[1:], lista2 +[lista[0]])
    else: return impares_aux(lista[1:], lista2)
    
