def factorial(Num):
    try:
        Num ==int(Num)
    except:
        return "Error: debe ser un numero entero"
    if Num>=0:
        return factorial_aux(Num)
    else:
        return"Error: numero debe ser un > 0"
def factorial_aux(N):
    if N == 0:
        return 1
    else:
        return N*factorial_aux(N-1)
    
