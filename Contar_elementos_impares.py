"""Contar los elementos impares de una lista
#E:Una lista con elementos numericos
#S:La suma de los elementos impares de la lista
#R: Que sea una la lista no este vacia y los elementos sean enteros
"""

def contar(lista):
    if not isinstance(lista,list) or lista==[]:
        return None
    else: return contar_aux(lista)

def contar_aux(lista):
    if lista==[]:
        return 0
    if lista[0]%2==0:
        return 0 + contar_aux(lista[1:])
    else:
        return 1 + contar_aux(lista[1:])