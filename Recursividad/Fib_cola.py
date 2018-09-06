"""
Cola
Fibonnaci
"""
def fib(N):
    if isinstance(N,int):
        if N>=0:
            return fib_aux(N,1,1,1)
        else:
            return "N debe ser >=0"
    else:
        return "N debe ser de tipo int"

def fib_aux(N,Cont,F1,F2):
    if N==Cont:
        return F2
    else:
        Cont = Cont + 1
        return fib_aux(N,Cont,F2, F1+ F2)
