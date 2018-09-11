def fib(num):
    if isinstance(num,int):
        if num>=0:
            return fib_aux(num)
        else: return "Debe ser mayor a cero"
    else:
        return 'Debe ser entero'
def fib_aux(num):
    if num <= 2:
        return num
    else: return fib_aux(num-1)+ fib_aux(num-2)