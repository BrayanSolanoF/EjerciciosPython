#Sumatoria
def sumatoria(N):
    if N <0:
        return"Error: limite debe ser mayor o igual a cero"
    else:
        return sumatoria_aux(N)

def sumatoria_aux(N):
    if N == 0:
        return 0
    else:
        return N + sumatoria_aux(N-1)
    
