##Calcular "e"
##Utilizo la funcion factorial y la funcion de portencia para "e"
def fact(N):
    if N == 0:
        return 1
    else:
        return N*fact(N-1)
def calc_e_aux(X,N):
    if N==0:
        return 1
    else:
        return pow(X,N)/fact(N)

"calc_e_aux(X,N-1)"
    
    
    






