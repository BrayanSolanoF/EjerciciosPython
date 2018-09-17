def suma(lista):
    if isinstance(lista,list):
        return suma_aux(lista)
    else: return "Debe ingresar los valores en forma de lista"
def suma_aux(lista):
    if lista ==[]:
        return 0
    else: return lista[0] + suma_aux(lista[1:])
