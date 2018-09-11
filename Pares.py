"""
-Programa: fun Det_numeros_pares
-Entradas: Numeros enteros en forma de lista
-Salidas: Nueva lista con numeros pares de la lista anterior
-Restricciones: Ingresar valores en forma de lista
-Version:1.0
"""
def pares(lista):
    if isinstance(lista,list)or lista!=[]:
        return pares_aux(lista, [])
    else:
        return "Error"

def pares_aux(lista,lista2):
    if lista == []:
        return lista2
    if lista[0] % 2 == 0:
        return pares_aux(lista[1:], lista2+[lista[0]])
    else: return pares_aux(lista[1:], lista2)


