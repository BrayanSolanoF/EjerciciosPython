"""
COLA
CALCULO DE FACTORIAL
"""
def fact(Num):
    if isinstance(Num, int):
        if Num ==1 or Num==0:
            return 1
        else:
            return fact_aux(Num, 1)
    else:
        return "Debe ser entero"
        
def fact_aux(Num,FactNum):
    if Num==1:
        return FactNum
    else:
        FactNum=Num*FactNum
        return fact_aux(Num-1,FactNum)
