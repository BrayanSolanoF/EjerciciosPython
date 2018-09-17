def contiene_cero(lista):
    if isinstance (lista, list):
        return contiene_cero_aux(lista)
    else: return "Debe ingresar los valores en forma de lista"
def contiene_cero_aux(lista):
    if lista==[]:
        return False
    elif lista[0]==0:
        return True
    else: return contiene_cero_aux(lista[1:])
