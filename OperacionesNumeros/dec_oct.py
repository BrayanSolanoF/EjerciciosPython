def dec_oct(Num):
    if isinstance(Num, int):
        return dec_oct_aux(Num,1)
    else: return "Error"
def dec_oct_aux(Num, factor):
    if  Num == 0:
        return 0
    else: return(Num%8*factor)+ dec_oct_aux(Num//8, factor*10)
####################################################################

def dec_bin(Num):
    if isinstance(Num, int):
        return dec_bin_aux(Num, 1)
    else: return "Error"

def dec_bin_aux(Num, factor):
    if Num==0:
        return 0
    else:
        return (Num%2*factor) + dec_bin_aux(Num//2, factor*10)
####################################################################

