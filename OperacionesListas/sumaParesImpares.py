def suma_pares_impares(lista):
    if isinstance (lista, list):
        return pares_aux(lista), impares_aux(lista)
    else: return "Ingresar valores en forma de lista"
def pares_aux(lista):
    if lista==[]:
        return 0
    elif lista[0]%2 ==0:
        return lista[0] + pares_aux(lista[1:])
    else: return pares_aux(lista[1:])
def impares_aux(lista):
    if lista==[]:
        return 0
    elif lista[0]%2!=0:
        return lista[0] + impares_aux(lista[1:])
    else: return impares_aux(lista[1:])
