def ceros(num):
    if isinstance(num, int):
        return ceros_aux(num)
    else: return "Error"
def ceros_aux(num):
    if num==0:
        return False
    elif num%10==0:
        return True
    else: return ceros_aux(num//10)
