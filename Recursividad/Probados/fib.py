#Fibonacci
#fib(n)= fib(n-1) + fib(n-2), para n = 2.3.5
def fib(N):
    if isinstance(N,int):
        if N>=0:
            return fib_aux(N)
        else:
            return "Error: N debe ser mayor o igual a 0"
    else:
        return "Error: N debe ser entero"
def fib_aux(N):
    if N < 2:
        return  N
    else:
        return fib_aux(N-1)+fib_aux(N-2) #Note dos llamadas a la funcion recursiva en la misma expresion.
