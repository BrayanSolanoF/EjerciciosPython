"""
Todo numero n mayor o igual que 8 se puede expresar
como una suma de treses y cincos. Es decir existen dos numeros a y b tal que :
N = 3*a + 5*b
Construya una funcion que dado un numero mayor que 8 los exprese en terminos
de treses y cincos.
"""
def new_num(Num):
    if isinstance(Num, int):
        if Num >= 8:
            return new_aux(Num)
