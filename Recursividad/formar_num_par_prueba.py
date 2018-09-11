def formar_par(num):
    if isinstance(num, int):
        return formar_par_aux(num)
    else: return 'Error'
def formar_par_aux(num):
    if num == 0:
        return 0
    else:
        digit = num%10
        if digit%2==1:
            return formar_par_aux(num//10)
        else:
            return digit + 10*formar_par_aux(num//10)

    