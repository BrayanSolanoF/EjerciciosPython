def oct_dec(Num):
    if isinstance(Num, int):
        return oct_dec_aux(Num,0)
    else: return "Error"
def oct_dec_aux(Num,factor):
    if Num==0:
        return 0
    else: return ((Num%10)*(8**factor))+ oct_dec_aux(Num//10, factor+1)
##################################################################
def bin_dec(Num):
    if isinstance(Num, int):
        return bin_dec_aux(Num,0)
    else: return "Error"
def bin_dec_aux(Num, factor):
    if Num == 0:
        return 0
    else: return ((Num%10)*(2**factor)) + bin_dec_aux(Num//10, factor+1)
