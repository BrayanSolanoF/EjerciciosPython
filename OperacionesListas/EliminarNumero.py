def eliminar(lista, num):
    if isinstance(lista, list) and isinstance(num, int):
        return eliminar_aux(lista, num)
    else: return "Debe ingresar valores validos :v"
def eliminar_aux(lista, num):
    if lista==[]:
        return []
    else:
        if lista[0]==num:
            return eliminar_aux(lista[1:], num)
        else: return [lista[0]] + eliminar_aux(lista[1:], num)
        
