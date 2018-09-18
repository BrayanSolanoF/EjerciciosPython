# Valores de N estaran en el intervalo [3,20]
#360º = 2π radianes = 6,283 radianes


def facto(X):
    try:
        X ==int(X)
    except:
        return "Error: debe ser un numero entero"
#X==2n
    if X>=0 and X<=20:
        return factorial_aux(X)
    else:
        return"Error: numero debe ser un > 0"
def factorial_aux(X):
    if X == 0:
        return 1
    else:
        return X*factorial_aux(X-1)

#####################################
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
####################################
def potencia(base, exp):
    if exp==0:
        return 1;
    elif exp==1:
        return base
    else:
        return base*potencia(base,exp-1)
######################################
def Cos(X,N):
    ((potencia(-1,N)/facto(2*N))





    
