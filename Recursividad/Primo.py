def primo(num):
    if isinstance(num, int):
        if num > 0:
            if num !=1:
                return primoAux(num, 2)
            else: return True
        else:
            return "Debe ser mayor a cero"
    else: return "Debe ser un entero"

def primoAux(num, div):
    if num == div:
        return True
    elif (num%div) == 0:
        return False
    else: return primoAux(num, div + 1)