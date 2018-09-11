"""
-Programa: fun Det_numeros_pares
-Entradas: Numeros enteros en forma de lista
-Salidas: Nueva lista con numeros pares de la lista anterior
-Restricciones: Ingresar valores en forma de lista
-Version:1.0
"""
def pares(lista):
    if isinstance(lista,list)or lista==[]:
        return pares_aux(lista)
    else:
        return "Error"

def pares_aux(lista):
    if lista!=[]:
        if lista[0]%2==0:
            return [lista[0]]+ pares_aux(lista[1:])
        else: return pares_aux(lista[1:])

    else: return[]

print(pares([1,2,5,6,8]))
