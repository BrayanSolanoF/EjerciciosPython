def fact(num):
    if isinstance(num,int):
        if num>=0:
            return fact_aux(num)
        else: return "Debe ser mayor a cero"
    else: return "Debe ser numero entero"
def fact_aux(num):
    if num == 0:
        return 1
    else: return num* fact_aux(num-1)