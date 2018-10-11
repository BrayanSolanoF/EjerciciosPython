
def tres_cinco(N):
    if isinstance(N,int) and N >=8:
        return tres_cinco_aux(N,0,0,0)
    else:
        return "Error"


def tres_cinco_aux(N,a,b,resultado):
    resultado = 3 * a + 5 * -b
    if resultado == N:
        return a,b 
    elif N%3 == 1:
        return 3 * a + 5 * -b,tres_cinco_aux(N,a+1,b,resultado)
    else:
        return "fdgd"


