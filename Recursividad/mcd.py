def mcd(A,B):
    if isinstance(A,int) and isinstance(B, int):
        if B<A:
            return mcd_aux(B,A)
        else:
            return mcd_aux(A,B)
    else: return "Deben ser numeros enteros"
def mcd_aux(A,B):
    if B ==0:
        return A
    else:
        return mcd_aux(B, A%B)