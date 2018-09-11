def dec_bin_aux(num, factor):
    if num==-0:
        return 0
    else:
        return (num%2*factor) + dec_bin_aux(num//2, factor*10)