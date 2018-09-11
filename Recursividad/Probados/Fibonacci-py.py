#Fibonacci
#fib(n)= fib(n-1)+ fib(n-2), para n = 2.3.5
def fibonacci(N):
    if isinstance(N,int):
        if N>=0:
            return fibonacci_aux(N)
        else:
            return "Error: N debe ser mayor o igual a 0"
    else:
        return "Error: N debe ser entero"
def fibonacci_aux(N):
    if N==0 or N==1:
        return 1
    else:
        return fibonacci_aux(N-1)+ fibonacci_aux(N-2)#Note dos llamadas a la funcion recursiva en la misma expresion.

